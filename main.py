import streamlit as st

import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import f1_score

st.set_page_config(page_title="Credit Card Approval", layout="wide")
st.header("Credit Card Approval Prediction Machine")
st.write("Paragraph")

@st.cache_data
def load_data():
    data = pd.read_csv("clean_dataset.csv")
    #st.write(data.head())

    features = data[["Gender", "Age", "Married", "Employed","YearsEmployed", "Income","BankCustomer", "PriorDefault", "Debt", "CreditScore"]]
    labels = data["Approved"]

    return features, labels

features, labels = load_data()

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.7, random_state= 42)

scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)

#st.write(features_train)

model = LogisticRegression(solver="liblinear")
model.fit(features_train, labels_train)

predictions = model.predict(features_test)

f1_score = round(f1_score(labels_test, predictions) * 100)
score = round(model.score(features_test, labels_test) * 100)

st.write("F1 Score: ", str(f1_score), " %")
st.write("Accuracy: ", str(score)," %")

form = st.form("user_inputs")

def normalize_data(gender, age, married, employed, yearsemployed, income, bankcustomer, priordefault, debt, creditscore):
    gender = 1 if gender.upper() == "MALE" else 0
    married = -1.9247195781581936 if married.upper() == "MARRIED" else 0.5195562051469969
    employed = -0.8857103130373326 if employed == "Yes" else 1.1290373221135228
    bankcustomer = -1.9247195781581936 if bankcustomer == "Yes" else 0.5195562051469969
    priordefault = -1.0857934280612735 if priordefault == "Yes" else 0.9209854970162591
    
    age = (age - 31.5) / 11.9
    debt = (debt - 4.76) / 4.97
    creditscore = ((creditscore - 300) / (850 - 350))
    income = (income - 1020) / 5210

    return [gender, age, married, employed, yearsemployed, income, bankcustomer, priordefault, debt, creditscore]


def user_inputs(form):
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

    submit = form.form_submit_button()

    if submit:
        normalized_inputs = normalize_data(gender, age, married, employed, yearsemployed, income, bankcustomer, priordefault, debt, creditscore)

        prediction = model.predict([normalized_inputs])

        #st.write(normalized_inputs)

        if prediction[0] == 1:
            st.subheader("Prediction: Approved :)")
        else:
            st.subheader("Prediction: Not Approved :(")

user_inputs(form)