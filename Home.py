import streamlit as st

# SET THE TITLE OF THE CURRENT OPEN PAGE
st.set_page_config(page_title="Home", layout="wide")
# WRITE A HEADER AND SOME TEXT
st.header("Welcome!")
st.write("This website is your one-stop destination for all things finance, technology, and innovation. Whether you're looking to optimize your budget, or explore the world of credit cards, we've got you covered!!")

# CREATE A DIVIDER
st.divider()

st.subheader("Services we offer:")
# USE STREAMLITS BUILT IN MARKDOWN FUNCTION TO ADD BULLET POINTS
st.markdown(
"""
- Budgeting Calculator
    - Learn about effective budgeting techniques, and discover our range of tools to help you reach your goals. 
- Credit Card Approval Detection
    - Discover our state-of-the-art credit card approval detection tool, which can help you make the necessary changes to your finance to be approved for a credit card.
"""
)
