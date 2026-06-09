# 🏥 Insurance Premium Predictor

A Machine Learning web app that predicts whether your insurance premium 
category will be **Low**, **Medium**, or **High** based on your health 
and lifestyle information.

## 🎯 Problem Statement
Insurance companies like PolicyBazaar categorize customers into risk 
groups to determine premium amounts. This project automates that 
classification using Machine Learning.

## 📊 Dataset
- **Source:** Machine Learning with R Datasets
- **Rows:** 1338
- **Features:** Age, Sex, BMI, Children, Smoker, Region

## 🔍 Key EDA Insights
- Smokers pay **4x more** than non-smokers
- BMI > 30 combined with smoking creates highest risk group
- Age increases charges for both smokers and non-smokers
- Southeast region has highest charges among smokers

## 🤖 Models Compared
| Model | Accuracy |
|-------|----------|
| SVM | 91.04% |
| Stacking | 91.04% |
| Gradient Boosting | 90.29% |
| Logistic Regression | 89.55% |
| Random Forest | 89.55% |
| Bagging | 89.92% |
| Decision Tree (Pre Pruning) | 89.92% |
| Decision Tree (Post Pruning) | 89.17% |
| AdaBoost | 89.17% |
| XGBoost | 89.17% |
| KNN | 88.05% |
| Voting | 88.80% |
| Naive Bayes | 75.37% |

## ⚙️ Feature Engineering
- Created `premium_category` (Low/Medium/High) from charges
- Created `smoker_obese` feature combining smoking + BMI > 30

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Matplotlib, Seaborn

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure
```
insurance_premium_predictor/
├── 01_EDA.ipynb
├── 02_model_building.ipynb
├── app.py
├── model.pkl
├── insurance.csv
├── insurance_encoded.csv
└── requirements.txt
```
