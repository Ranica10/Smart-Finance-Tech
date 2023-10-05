# IMPORT ALL THE NECESSARY LIBRARIES
import streamlit as st

import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# SET THE TITLE OF THE CURRENT OPEN PAGE
st.set_page_config(page_title="Credit Card Approval", layout="wide")
st.header("Credit Card Approval Prediction Machine")
st.write("Your credit score is a crucial factor in your financial life. Fill in the form below to see if you qualify for a credit card!!")

st.divider()

# USE PANDAS LIBRARY TO READ THE CSV DOCUMENT CONTAINING THE DATASET
data = pd.read_csv("clean_dataset.csv")
#st.write(data.head())

# SPILT THE DATA INTO FEATURES (INPUTS) AND LABELS (OUTPUTS)
features = data[["Gender", "Age", "Married", "Employed","YearsEmployed", "Income","BankCustomer", "PriorDefault", "Debt", "CreditScore"]]
labels = data["Approved"]

# USE SKLEARN LIBRARY TO SPILT THE DATA INTO A TRAINING SET AND A TESTING SET
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.7, random_state= 42)

# NORMALIZE THE DATA SO THAT EVERY FEATURE IS WEIGHTED EQUALLY
scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)

#st.write(features_train)

# USE A LOGISTIC REGRESSION ALGORITIM TO FIT THE MODEL TOO
model = LogisticRegression(solver="liblinear")
model.fit(features_train, labels_train)

# USE THE TESTING DATA TO COMPARE THE PREDICTED OUTPUTS WITH THE ACTUAL TO FIND THE ACCURACY OF THE MODEL
predictions = model.predict(features_test)
score = round(model.score(features_test, labels_test) * 100)

st.caption("NOTE: THIS MODEL WAS TRAINED WITH A DATASET, AND IS NOT 100% ACCURATE")
st.write("Accuracy: ", str(score)," %")

# DECLARE A FORM THAT THE USER WILL FILL OUT
form = st.form("user_inputs")

def normalize_data(gender, age, married, employed, yearsemployed, income, bankcustomer, priordefault, debt, creditscore):
    # CONVERT THE INPUTS TO BINARY VARIABLES THAT CAN BE READ BY THE DATASET
    gender = 1 if gender.upper() == "MALE" else 0
    married = -1.9247195781581936 if married.upper() == "MARRIED" else 0.5195562051469969
    # THE FOLLOWING NUMBERS WERE OBTAINED FROM THE NORMALIZED DATASET THROUGH THEIR STANDARD DEVIATION (DISPLAYED THROUGH COMMENTED LINE 34)
    employed = -0.8857103130373326 if employed == "Yes" else 1.1290373221135228
    bankcustomer = -1.9247195781581936 if bankcustomer == "Yes" else 0.5195562051469969
    priordefault = -1.0857934280612735 if priordefault == "Yes" else 0.9209854970162591

    # NORMALIZE THE NUMERIC DATA TO MATCH THE TRAINING SET USED EARLIER THROUGH THEIR MIN AND MAX VALUES (MINMAXSCALER ALGORITHM)
    age = (age - 31.5) / 11.9
    debt = (debt - 4.76) / 4.97
    creditscore = ((creditscore - 300) / (850 - 350))
    income = (income - 1020) / 5210

    # RETURN THE NORMALIZED USER INPUTS
    return [gender, age, married, employed, yearsemployed, income, bankcustomer, priordefault, debt, creditscore]

def user_inputs(form):
    # TAKE IN THE USER INPUTS THROUGH THE FORM ELEMENT AND SAVE THEM TO THEIR CORROSPONDING VARIABLES
    gender = form.text_input("Gender (MALE/FEMALE)")
    age = form.number_input("Age", step = 1, min_value = 18)
    married = form.text_input("Marital Status (SINGLE/MARRIED)")
    employed = form.radio("Employed?", options=["Yes", "No"])
    yearsemployed = form.number_input("Number of Years Employed", step = 1, min_value = 0)
    bankcustomer = form.radio("Current Bank Customer?", options=["Yes", "No"])
    income = form.number_input("Income")
    priordefault = form.radio("Any Prior Defaults?", options=["Yes", "No"])
    debt = form.number_input("Debt")
    creditscore = form.slider("Credit Score", max_value=850, min_value=300)

    # CREATE A SUBMIT BUTTON
    submit = form.form_submit_button()

    # IF THE SUBMIT BUTTON WAS CLICKED, RUN THE NORMALIZE_DATA FUNCTION TO SCALE THE USER INPUTS
    if submit:
        normalized_inputs = normalize_data(gender, age, married, employed, yearsemployed, income, bankcustomer, priordefault, debt, creditscore)

        # USE SKLEARN LIBRARY BUILT IN PREDICT FUNCTION TO PREDICT AN OUTPUT FOR THE USER INPUTS AND SAVE IT TO A VARIABLE
        prediction = model.predict([normalized_inputs])
        # RETURN THIS VALUE TO BE ACCESSED OUTSIDE THE FUNCTION
        return prediction
        #st.write(normalized_inputs)

# SAVE THE PREDICTION OUTSIDE THE FUNCTION AFTER CALLING IT
prediction = user_inputs(form)

# IF THE PREDICTION IS THE BINARY VALUE 1 (REPRESENTS YES), DISPLAY THE PREDICTION IS APPROVED
if prediction == 1:
    st.subheader("Prediction: Approved :)")
# IF THE PREDICTION IS THE BINARY VALUE 0 (REPRESENTS NO), DISPLAY THE PREDICTION IS NOT APPROVED
elif (prediction == 0):
    st.subheader("Prediction: Not Approved :(")

st.divider()

st.header("Credit Score Improvement")

# USE STREAMLITS BUILT IN MARKDOWN FUNCTION TO ADD BULLET POINTS
st.markdown(
"""
A good credit score can save you money on loans, mortgages, and credit card interest rates. Here are some strategies to help you improve your credit score:
- Pay Your Bills on Time
    - Timely payments are the most significant factor affecting your credit score. Set up automatic payments or reminders to ensure you pay all bills on time.
- Reduce Credit Card Balances
    - Aim to keep your credit card balances below 30% of your credit limit. High credit utilization can negatively impact your credit score.
- Handle Collections and Late Payments
    - If you have collections or late payments, try negotiating with the creditors to settle the debt or set up a payment plan.
"""
)
