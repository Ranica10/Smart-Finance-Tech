import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Budgeting Calculator", layout="wide")
st.header("Budgeting Calculator")
st.write("Embark on a journey of financial planning via the form below to help you take control of your finances!!")

display_chart_var = False

def display_chart(mortgage, rent, maintenance, internet, utilities, carloan, gas, insurance, 
                       repairs, tuition, studloan, supplies, groceries, entertainment, clothing, medical, other):
    housing_expenses = mortgage + rent + maintenance + internet + utilities
    transportation_expenses = carloan + gas + insurance + repairs
    educational_expenses = tuition + studloan + supplies
    food_personal_expenses = groceries + entertainment + clothing + medical + other

    # Data for the pie chart
    values = [housing_expenses, transportation_expenses, educational_expenses, food_personal_expenses]

    labels = ['Housing Expenses', 'Transportation Expenses', 'Educational Expenses', 'Food and Personal Expenses']

    display_chart_var = True

    return values, labels, display_chart_var

with st.form("user_inputs"):
    st.subheader("Monthly Income")
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

    submit = st.form_submit_button()

    if submit:
        values, labels, display_chart_var = display_chart(mortgage, rent, maintenance, internet, utilities, carloan, gas, insurance, 
                       repairs, tuition, studloan, supplies, groceries, entertainment, clothing, medical, other)

st.header("Results:")

st.divider()

if display_chart_var:
    st.subheader("Monthly Expenses by Category:")

    # Plotting the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))

    # The percentages will be set to one significant digit using autopct
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

    # Display the chart using st.pyplot()
    st.pyplot(fig)
    st.divider()

    st.subheader("Net Income")

    netincome = salary + otherincome

    # Go through every expenses catogory and subtract it from the salary + other income sources
    for i in range(len(values)):
        netincome -= values[i]

    st.write("$" ,str(float(netincome)))

    if (netincome > 0):
        st.write("Looks like you're above your budget. Good Job!!")
    else:
        st.write("--- Looks like you might be over budget. Scroll below for some tips and tricks!! ---")

    st.divider()

st.header("Budget Improvement Tips")
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