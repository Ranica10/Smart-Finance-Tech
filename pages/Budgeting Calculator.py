# IMPORT ALL THE NECESSARY LIBRARIES
import streamlit as st
import matplotlib.pyplot as plt

# SET THE TITLE OF THE CURRENT OPEN PAGE
st.set_page_config(page_title="Budgeting Calculator", layout="wide")
st.header("Budgeting Calculator")
st.write("Embark on a journey of financial planning via the form below to help you take control of your finances!!")

# CREATE A VARIABLE TO CHECK IF THE INPUTS ARE FILLED IN TO NOT RUN THE PI CHART ON LOAD (CREATES AN ERROR)
display_chart_var = False

def display_chart(mortgage, rent, maintenance, internet, utilities, carloan, gas, insurance, 
                       repairs, tuition, studloan, supplies, groceries, entertainment, clothing, medical, other):
    # SPLIT THE USER INPUTS INTO FOUR CATEGORIES WITH THEIR CORROSPONDING SUMS
    housing_expenses = mortgage + rent + maintenance + internet + utilities
    transportation_expenses = carloan + gas + insurance + repairs
    educational_expenses = tuition + studloan + supplies
    food_personal_expenses = groceries + entertainment + clothing + medical + other

    # SAVE THE DATA FOR THE PI CHART IN A VARIABLE AS A LIST
    values = [housing_expenses, transportation_expenses, educational_expenses, food_personal_expenses]
    # SAVE THE LABELS (CATERGORIES) FOR THE PI CHART AS A LIST
    labels = ['Housing Expenses', 'Transportation Expenses', 'Educational Expenses', 'Food and Personal Expenses']

    # SET THE GLOBAL VARIABLE AS TRUE TO TELL THE PROGRAM THAT THE INPUTS WERE ALL FILLED IN
    display_chart_var = True

    # RETURN THE DATA, LABELS, AND GLOBAL VARIABLE
    return values, labels, display_chart_var

with st.form("user_inputs"):
    # USE STREAMLIT BUILT IN FUNCTION TO SPILT THE FORM INTO THE FOUR CATEGORIES
    st.subheader("Monthly Income")
    # TAKE IN THE USER INPUTS THROUGH THE FORM ELEMENT AND SAVE THEM TO THEIR CORROSPONDING VARIABLES
    salary = st.number_input("Salary", min_value = float(0), value=float(0))
    otherincome = st.number_input("Other Income", min_value = float(0), value=float(0))

    st.divider()

    st.subheader("Housing Expenses")
    mortgage = st.number_input("Mortgage", min_value = float(0), value=float(0))
    rent = st.number_input("Rent", min_value = float(0), value=float(0))
    maintenance = st.number_input("Maintenance", min_value = float(0), value=float(0))
    internet = st.number_input("Internet/TV", min_value = float(0), value=float(0))
    utilities = st.number_input("Utilities", min_value = float(0), value=float(0))

    st.divider()

    st.subheader("Transportation Expenses")
    carloan = st.number_input("Loan Payment", min_value = float(0), value=float(0))
    gas = st.number_input("Fuel/Gas", min_value = float(0), value=float(0))
    insurance = st.number_input("Insurance", min_value = float(0), value=float(0))
    repairs = st.number_input("Repairs", min_value = float(0), value=float(0))

    st.divider()

    st.subheader("Educational Expenses")
    tuition = st.number_input("Tuition", min_value = float(0), value=float(0))
    studloan = st.number_input("Student Loans", min_value = float(0), value=float(0))
    supplies = st.number_input("School Supplies", min_value = float(0), value=float(0))

    st.divider()
    st.subheader("Food and Personal Expenses")
    groceries = st.number_input("Groceries", min_value = float(0), value=float(0))
    entertainment = st.number_input("Entertainment", min_value = float(0), value=float(0))
    clothing = st.number_input("Clothing", min_value = float(0), value=float(0))
    medical = st.number_input("Medical", min_value = float(0), value=float(0))
    other = st.number_input("Other Expenses", min_value = float(0), value=float(0))

    # CREATE A SUBMIT BUTTON
    submit = st.form_submit_button()

    # IF THE SUBMIT BUTTON WAS CLICKED, RUN THE DISPLAY_CHART FUNCTION ABOVE TO GET THE PI CHART DATA AND LABELS
    if submit:
        # SAVE THE OUTPUTS TO VARIABLES TO BE ACCESSED OUTSIDE THE FUNCTIONS
        values, labels, display_chart_var = display_chart(mortgage, rent, maintenance, internet, utilities, carloan, gas, insurance, 
                       repairs, tuition, studloan, supplies, groceries, entertainment, clothing, medical, other)

st.header("Results:")

st.divider()

# CHECKS IF THE VARIABLE IS TRUE (SET IF THE USER INPUTTED VALUES INTO THE FORM), AND THEN DISPLAYS THE CHART USING THE DATA AND LABELS
if display_chart_var:
    st.subheader("Monthly Expenses by Category:")

    # PLOTTING THE PI CHART AS A WINDOW THAT CONTAINS THE PLOT
    fig, ax = plt.subplots(figsize=(8, 8))

    # THE PERCENTAGES IN THE CHART WILL BE SET TO ONE SIGNIFICANT DIGIT USING AUTOPCT
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

    # DISPLAY THE CHART USING MATHPLOTLIB BUILT IN FUNCTION
    st.pyplot(fig)
    st.divider()

    st.subheader("Net Income")

    # CALCULATE THE NET INCOME OF THE USER
    netincome = salary + otherincome

    # GO THROUGH ALL THE EXPENSES CATEGORIES AND SUBTRACT THEIR SUMS FROM THE SALARY AND OTHER INCOME SOURCES
    for i in range(len(values)):
        netincome -= values[i]

    # DISPLAY THE NET INCOME TO THE USER
    st.write("$" ,str(float(netincome)))

    # ADDS A PERSONALIZED MESSAGE BASED ON WHETHER THE USER IS ABOVE OR BELOW THEIR BUDGET
    if (netincome > 0):
        st.write("Looks like you're above your budget. Good Job!!")
    else:
        st.write("--- Looks like you might be over budget. Scroll below for some tips and tricks!! ---")

    st.divider()

st.header("Budget Improvement Tips")

# USE STREAMLITS BUILT IN MARKDOWN FUNCTION TO ADD BULLET POINTS
st.markdown(
"""
Managing a budget and staying within it is crucial for financial stability. If you find yourself going over budget, here are some tips and tricks to help you get back on track:
- Prioritize Essential Expenses
    - Ensure that essential expenses like housing, utilities, groceries, and debt payments are covered first.
- Find Alternative Transportation
    - Consider walking, biking, carpooling, or using public transportation to save on fuel and parking costs.
- Review Subscriptions
    - Cancel or temporarily suspend subscriptions you don't use frequently, like streaming services, magazines, or gym memberships.
"""
)
