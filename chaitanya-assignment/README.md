# Assignment 2 — Finding the Best Pre-trained Model for Text Generation
### Applying TOPSIS to Select the Best Regression Model for Hospital Queue Simulation

**Roll Number:** 102316004  
**Task:** Text Generation (Roll Numbers ending with 1 or 6)

---

## 📌 Overview

This assignment applies the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** decision-making framework to evaluate and rank multiple machine learning regression models. The objective is to predict the **average patient waiting time** in a simulated hospital queue system, and then select the best model using multi-criteria evaluation.

---

## 🔬 Methodology

### Step 1: Hospital Queue Simulation (SimPy)

A discrete-event simulation was built using **SimPy** to generate synthetic data for a hospital queue system. The simulation models:

- **Arrival Rate** (patients/unit time) — sampled uniformly from `[2, 10]`
- **Service Rate** (patients/unit time) — sampled uniformly from `[5, 15]`
- **Number of Servers** — sampled uniformly from `[1, 5]`

**1000 simulation runs** were executed (seeded with Roll Number `102316004`) to generate a diverse dataset. Each run recorded the **average waiting time** as the target variable.

The dataset was saved as:  
📄 `simulation_data_102316004.csv`

---

### Step 2: Machine Learning Model Training

The dataset was split into **80% training / 20% testing**. Eight regression models were trained and evaluated:

| Model | Description |
|---|---|
| Linear Regression | Baseline linear model |
| Decision Tree | Non-linear tree-based model |
| Random Forest | Ensemble of decision trees |
| Gradient Boosting | Sequential boosting ensemble |
| Extra Trees | Randomized ensemble method |
| SVR | Support Vector Regression |
| KNN | K-Nearest Neighbors Regressor |
| XGBoost | Extreme Gradient Boosting |

---

### Step 3: Model Evaluation Metrics

Each model was evaluated on four metrics:

| Metric | Description | Preference |
|---|---|---|
| **R² Score** | Coefficient of determination | Higher is better |
| **MSE** | Mean Squared Error | Lower is better |
| **RMSE** | Root Mean Squared Error | Lower is better |
| **MAE** | Mean Absolute Error | Lower is better |

#### Results Table

| Model | R² Score | MSE | RMSE | MAE |
|---|---|---|---|---|
| **XGBoost** | **0.9732** | **0.2457** | **0.4957** | **0.0919** |
| Random Forest | 0.9543 | 0.4194 | 0.6476 | 0.1120 |
| Decision Tree | 0.9270 | 0.6698 | 0.8184 | 0.1357 |
| Gradient Boosting | 0.9052 | 0.8702 | 0.9328 | 0.2305 |
| Extra Trees | 0.8815 | 1.0876 | 1.0429 | 0.1647 |
| KNN | 0.8692 | 1.2010 | 1.0959 | 0.2105 |
| SVR | 0.0805 | 8.4405 | 2.9052 | 0.4387 |
| Linear Regression | 0.0619 | 8.6103 | 2.9343 | 1.4013 |

---

## 📊 Visualizations

### R² Score Comparison
![R2 Score Comparison](mae_plot_102316004%20(1)-c1.png)

### MSE Comparison
![MSE Comparison](mse_plot_102316004%20(1)-c1.png)

### RMSE Comparison
![RMSE Comparison](rmse_plot_102316004%20(1)-c1.png)

### MAE Comparison
![MAE Comparison](r2_plot_102316004%20(1)-c1.png)

---

## 🏆 TOPSIS-Based Model Ranking

TOPSIS was applied using all four metrics (R², MSE, RMSE, MAE) with appropriate benefit/cost weights to compute a final performance score for each model:

- **R²** → Benefit criterion (maximize)
- **MSE, RMSE, MAE** → Cost criteria (minimize)

### 🥇 Best Model: **XGBoost**

XGBoost achieved the highest TOPSIS score due to:
- Highest **R² Score**: `0.9732`
- Lowest **MSE**: `0.2457`
- Lowest **RMSE**: `0.4957`
- Lowest **MAE**: `0.0919`

---

## 🛠️ Libraries Used

```python
import simpy          # Discrete-event simulation
import numpy as np    # Numerical computing
import pandas as pd   # Data manipulation
import matplotlib.pyplot as plt  # Visualization

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
```

---

## 📁 Output Files

| File | Description |
|---|---|
| `simulation_data_102316004.csv` | Raw simulation data (1000 runs) |
| `r2_plot_102316004.png` | R² Score bar chart |
| `mse_plot_102316004.png` | MSE bar chart |
| `rmse_plot_102316004.png` | RMSE bar chart |
| `mae_plot_102316004.png` | MAE bar chart |

---

## ✅ Conclusion

Using the TOPSIS multi-criteria decision analysis, **XGBoost** was identified as the best model for predicting hospital queue waiting times. It outperformed all other models across all four evaluation metrics, making it the optimal choice for this regression task.
