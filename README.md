# Customer Churn Prediction App 📊

An end-to-end Machine Learning project that predicts whether a bank customer is likely to churn using customer banking and demographic information.

This project covers the complete ML workflow including:
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Model training and evaluation
- Model comparison
- Pipeline creation
- Streamlit web app deployment

---

# 📌 Project Overview

Customer churn prediction is one of the most important business problems in the banking industry. Retaining existing customers is often more cost-effective than acquiring new ones.

This application predicts customer churn using Machine Learning models trained on banking customer data.

---

# 🧠 Machine Learning Workflow

The project follows a complete end-to-end ML pipeline:

```text
Data Collection
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis (EDA)
       ↓
Feature Engineering
       ↓
Data Preprocessing
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Selection
       ↓
Model Deployment
```

---

# 📂 Dataset Features

The dataset contains customer banking information such as:

| Feature | Description |
|---|---|
| CreditScore | Customer credit score |
| Geography | Customer country |
| Gender | Male/Female |
| Age | Customer age |
| Tenure | Years with bank |
| Balance | Bank balance |
| NumOfProducts | Number of bank products |
| HasCrCard | Credit card ownership |
| IsActiveMember | Active membership status |
| EstimatedSalary | Estimated yearly salary |
| Exited | Target variable (Churn) |

---

# 📊 Exploratory Data Analysis (EDA)

Performed detailed EDA to identify:
- Customer churn distribution
- Correlation between features
- Impact of geography on churn
- Age and balance patterns
- Active membership behavior
- Feature relationships

## Key Insights
- Older customers showed higher churn probability
- Inactive members were more likely to churn
- Geography influenced customer churn patterns
- Ensemble models significantly improved performance

---

# 🤖 Models Used

The following machine learning models were trained and evaluated:

| Model | ROC-AUC Score |
|---|---|
| Logistic Regression | 0.777 |
| Decision Tree | 0.838 |
| Random Forest | 0.865 |
| Gradient Boosting | 0.871 |

## Final Selected Model
✅ Gradient Boosting Classifier

---

# ⚙️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

# 🖥️ Streamlit App Features

- Interactive dashboard UI
- Real-time churn prediction
- Churn probability score
- Risk level indicator
- Custom dark theme
- Customer input sidebar
- ML model integration

---

# ▶️ Installation & Run Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
```

## 2️⃣ Move Into Project Folder

```bash
cd customer-churn-prediction
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📈 Model Evaluation

The final Gradient Boosting model achieved:

- ROC-AUC Score: **0.871**
- Strong balance between precision and recall
- Improved churn detection performance
- Better generalization than baseline models

---

# 📌 Future Improvements

- Hyperparameter tuning
- Feature importance visualization
- Docker deployment
- FastAPI backend integration
- Cloud deployment
- SHAP explainability
- Real-time database integration

---

# 👨‍💻 Author

Aditya Rothe

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub and connect with me on LinkedIn!
