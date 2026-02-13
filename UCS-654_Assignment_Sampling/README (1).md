# Sampling Techniques and Machine Learning Model Comparison

## 📌 Project Description
This project analyzes the impact of different sampling techniques on the performance of various machine learning models using a credit card dataset. The dataset initially suffers from class imbalance, which is handled using oversampling techniques.

---

## 📂 Dataset
- **Name:** Creditcard_data.csv  
- **Target Variable:** Class  
- **Problem Type:** Binary Classification  
- **Issue:** Class Imbalance  

---

## ⚙️ Steps Performed

### 1️⃣ Data Loading
The dataset is loaded and split into features and target variables.

### 2️⃣ Handling Class Imbalance
- **Technique Used:** SMOTE (Synthetic Minority Over-sampling Technique)
- The dataset is balanced by generating synthetic minority class samples.

### 3️⃣ Sample Creation
Five different samples are created from the balanced dataset.

### 4️⃣ Sampling Techniques Applied
- Simple Random Sampling  
- Stratified Sampling  
- K-Fold Sampling  
- Bootstrap Sampling  
- Cluster Sampling  

### 5️⃣ Machine Learning Models Used
- Logistic Regression  
- Decision Tree  
- Random Forest  
- K-Nearest Neighbors  
- Support Vector Machine  

### 6️⃣ Evaluation Metric
- Accuracy Score

---

## 📊 Output
- Comparison table showing accuracy of each model under different sampling techniques
- Identification of best sampling technique per model

---

## 🧠 Conclusion
Different sampling techniques affect model performance differently. Stratified and K-Fold sampling generally provide better generalization, while simple random sampling works well for ensemble models.

---

## 🛠 Libraries Used
- pandas  
- numpy  
- scikit-learn  
- imbalanced-learn  
- matplotlib  

---
