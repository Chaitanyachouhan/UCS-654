from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import smtplib
import os
from email.message import EmailMessage
import re
import tempfile
import io

app = Flask(__name__)


def topsis(df, weights, impacts):

    data = df.iloc[:, 1:].values.astype(float)
    norm = np.sqrt((data ** 2).sum(axis=0))

    # Prevent division by zero
    if np.any(norm == 0):
        raise ValueError("Division by zero encountered during normalization.")

    normalized = data / norm

    weights = np.array(weights)
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(np.max(weighted[:, i]))
            ideal_worst.append(np.min(weighted[:, i]))
        else:
            ideal_best.append(np.min(weighted[:, i]))
            ideal_worst.append(np.max(weighted[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    return df


def valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def send_email(receiver, filepath):
    sender_email = "chaitanyachouhan7@gmail.com"
    app_password = "wtxjvjmhhjxoplpq"

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender_email
    msg["To"] = receiver
    msg.set_content("Please find the attached TOPSIS result.")

    with open(filepath, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(filepath)

    msg.add_attachment(file_data, maintype="application",
                       subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["file"]
        weights_input = request.form["weights"]
        impacts_input = request.form["impacts"]
        email = request.form["email"]

        # Email validation
        if not valid_email(email):
            return "Invalid Email Format"

        # File validation
        if file.filename == "":
            return "No file selected"

        if not file.filename.lower().endswith(".csv"):
            return "Only CSV files are supported. Please upload a .csv file."

        # Safe CSV reading with auto delimiter detection
        try:
            file_content = file.read()
            file.seek(0)
            df = pd.read_csv(io.BytesIO(file_content), sep=None, engine="python")
        except Exception as e:
            return f"Error reading CSV file: {str(e)}"

        # Check minimum columns
        if df.shape[1] < 3:
            return f"Input file must contain at least 3 columns. Detected {df.shape[1]} columns."

        # Check numeric columns
        try:
            df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
        except:
            return "From 2nd column onwards must contain numeric values only."

        weights = weights_input.split(",")
        impacts = impacts_input.split(",")

        if len(weights) != len(impacts) or len(weights) != (df.shape[1] - 1):
            return f"Number of weights and impacts must match number of criteria columns ({df.shape[1] - 1})."

        try:
            weights = [float(w) for w in weights]
        except:
            return "Weights must be numeric."

        if not all(i in ["+", "-"] for i in impacts):
            return "Impacts must be either + or -."

        try:
            result = topsis(df, weights, impacts)
        except Exception as e:
            return f"Error during TOPSIS calculation: {str(e)}"

        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        result.to_csv(temp.name, index=False)

        try:
            send_email(email, temp.name)
        except:
            return "Failed to send email. Please check email configuration."

        return "Result sent to email successfully!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
