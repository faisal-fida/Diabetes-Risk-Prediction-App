# diabetes_app.py

# imports
import pandas as pd
import joblib
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# Create virtual environment:
# python3 -m venv venv
# In your virtual environment:
# python3 -m pip install --upgrade pip
# python -m pip install -U autopep8
# pip install pandas
# pip install joblib
# pip install streamlit
# pip install scikit-learn
# streamlit run diabetes_app.py

# Header
st.write(
    """
# Diabetes Risk Prediction App
Answer 6 questions to find out if you may be at risk for Type II Diabetes.
"""
)

with st.expander("About this App:"):
    st.write(
        """
    * Model Inputs: Utilizes data like weight, height, age, and health conditions, converting weight and height to BMI.
    * Training Data: Relies on survey responses from the CDC's Behavioral Risk Factor Surveillance System to train a Decision Tree model.
    * App Objective: Designed for public awareness, not for diagnosis; encourages individuals at risk or with prediabetes to seek medical advice.
    * BRFSS Overview: Established in 1984, BRFSS conducts extensive health-related telephone surveys across all 50 states and territories.
    * Performance Metrics: The model exhibits a 70% accuracy rate with a focus on high recall, aligning with the goal of identifying as many potential diabetes cases as possible.
    """
    )

st.write("### Answer Questions to predict:")

col1, col2, col3 = st.columns(3)

weight = col1.number_input("1. Weight (lbs)", min_value=50, max_value=999, value=190)

height = col2.number_input("2. Height (inches): ", min_value=36, max_value=95, value=68)

age = col3.selectbox(
    "3. Age:",
    (
        "Age 18 to 24",
        "Age 25 to 29",
        "Age 30 to 34",
        "Age 35 to 39",
        "Age 40 to 44",
        "Age 45 to 49",
        "Age 50 to 54",
        "Age 55 to 59",
        "Age 60 to 64",
        "Age 65 to 69",
        "Age 70 to 74",
        "Age 75 to 79",
        "Age 80 or older",
    ),
    index=4,
)

highchol = col1.selectbox(
    "4. High Cholesterol: ",
    ("Yes", "No"),
    index=1,
)

highbp = col2.selectbox(
    "5. High Blood Pressure: ",
    ("Yes", "No"),
    index=0,
)

genhlth = col3.selectbox(
    "6. General Health: ",
    ("Excellent", "Very Good", "Good", "Fair", "Poor"),
    index=3,
)
df1 = pd.DataFrame(
    [[round(weight), round(height), age, highchol, highbp, genhlth]],
    columns=["Weight", "Height", "Age", "HighChol", "HighBP", "GenHlth"],
)


def calculate_bmi(weight, height):
    bmi = round((703 * weight) / (height**2))
    return bmi


def prep_df(df):
    df["BMI"] = df.apply(
        lambda row: calculate_bmi(row["Weight"], row["Height"]), axis=1
    )
    df = df.drop(columns=["Weight", "Height"])
    df = df[["BMI", "Age", "HighChol", "HighBP", "GenHlth"]]
    df["Age"] = df["Age"].replace(
        {
            "Age 18 to 24": 1,
            "Age 25 to 29": 2,
            "Age 30 to 34": 3,
            "Age 35 to 39": 4,
            "Age 40 to 44": 5,
            "Age 45 to 49": 6,
            "Age 50 to 54": 7,
            "Age 55 to 59": 8,
            "Age 60 to 64": 9,
            "Age 65 to 69": 10,
            "Age 70 to 74": 11,
            "Age 75 to 79": 12,
            "Age 80 or older": 13,
        }
    )
    df["HighChol"] = df["HighChol"].replace({"Yes": 1, "No": 0})
    df["HighBP"] = df["HighBP"].replace({"Yes": 1, "No": 0})
    df["GenHlth"] = df["GenHlth"].replace(
        {"Excellent": 1, "Very Good": 2, "Good": 3, "Fair": 4, "Poor": 5}
    )

    return df


df = prep_df(df1)

with st.expander("User inputs"):
    st.write("**User Inputs** ", df1)
with st.expander("Decision Tree Inputs"):
    st.write("**User Inputs Prepared for Decision Tree** ", df)

model = joblib.load("app\model.pkl")

if st.button("Predict your Risk"):
    prediction = model.predict(df)
    prediction_probability = model.predict_proba(df)
    low_risk_proba = round(prediction_probability[0][0] * 100)
    high_risk_proba = round(prediction_probability[0][1] * 100)

    if prediction[0] == 0:
        st.write("You are at **low-risk** for prediabetes")
        st.write("Low-risk probality", low_risk_proba, "%")
        st.write("High-risk probality", high_risk_proba, "%")
    else:
        st.write("You are at **high-risk** for prediabetes")
        st.write("Low-risk probality", low_risk_proba, "%")
        st.write("High-risk probality", high_risk_proba, "%")
