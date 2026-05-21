import streamlit as st
import pandas as pd
import joblib
import numpy as np

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
model = joblib.load("customer_churn_model.pkl")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    background-color: #ff4b4b;
    color: white;
}

.stButton>button:hover {
    background-color: #ff2e2e;
    color: white;
}

.metric-card {
    background-color: #262730;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("📊 Customer Churn Prediction App")

st.markdown("""
Predict whether a bank customer is likely to churn using a Machine Learning model.
""")

st.markdown("---")

# =========================
# SIDEBAR
# =========================
st.sidebar.header("📝 Customer Information")

credit_score = st.sidebar.slider(
    "Credit Score",
    300,
    900,
    650
)

geography = st.sidebar.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.sidebar.slider(
    "Age",
    18,
    100,
    35
)

tenure = st.sidebar.slider(
    "Tenure",
    0,
    10,
    5
)

balance = st.sidebar.number_input(
    "Balance",
    min_value=0.0,
    value=50000.0
)

num_products = st.sidebar.slider(
    "Number of Products",
    1,
    4,
    1
)

has_card = st.sidebar.selectbox(
    "Has Credit Card",
    [0, 1]
)

active_member = st.sidebar.selectbox(
    "Is Active Member",
    [0, 1]
)

salary = st.sidebar.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=50000.0
)

# =========================
# CREATE INPUT DATAFRAME
# =========================
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Geography': [geography],
    'Gender': [gender],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_products],
    'HasCrCard': [has_card],
    'IsActiveMember': [active_member],
    'EstimatedSalary': [salary]
})

# =========================
# MAIN LAYOUT
# =========================
left_col, right_col = st.columns([1, 1])

# =========================
# PREDICTION BUTTON
# =========================
with left_col:

    st.subheader("🔍 Prediction")

    if st.button("Predict Customer Churn"):

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        probability_percent = probability * 100

        # =========================
        # RESULT
        # =========================
        if prediction == 1:

            st.error("⚠️ Customer is likely to churn")

        else:

            st.success("✅ Customer is likely to stay")

        # =========================
        # METRICS
        # =========================
        metric_col1, metric_col2 = st.columns(2)

        with metric_col1:
            st.metric(
                "Churn Probability",
                f"{probability_percent:.2f}%"
            )

        with metric_col2:
            st.metric(
                "Risk Score",
                f"{probability_percent:.1f}/100"
            )

        # =========================
        # PROGRESS BAR
        # =========================
        st.subheader("📈 Churn Risk Level")

        st.progress(int(probability_percent))

        # =========================
        # RISK LEVEL
        # =========================
        if probability < 0.3:

            st.success("🟢 Low Churn Risk")

        elif probability < 0.7:

            st.warning("🟡 Medium Churn Risk")

        else:

            st.error("🔴 High Churn Risk")

# =========================
# CUSTOMER DATA
# =========================
with right_col:

    st.subheader("📋 Customer Information")

    st.dataframe(
        input_data,
        use_container_width=True
    )

    st.subheader("📌 Model Information")

    st.info("""
    Model Used: Gradient Boosting Classifier
    
    This machine learning model predicts customer churn
    based on banking customer information.
    """)

# =========================
# ABOUT SECTION
# =========================
st.markdown("---")

st.subheader("📖 About This Project")

st.markdown("""
This project is an end-to-end Machine Learning application built using:

- Python
- Scikit-learn
- Streamlit
- Pandas
- NumPy

The model predicts whether a bank customer is likely to churn based on customer demographics and banking activity.
""")

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown(
    "<center>Built with ❤️ by Aditya Rothe</center>",
    unsafe_allow_html=True
)