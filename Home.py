import streamlit as st

st.set_page_config(page_title="Home", layout="wide")
st.header("Welcome!")
st.write("This website is your one-stop destination for all things finance, technology, and innovation. Whether you're looking to optimize your budget, or explore the world of credit cards, we've got you covered!!")

st.divider()

st.subheader("Services we offer:")
st.markdown(
"""
- Budgeting Calculator
    - Learn about effective budgeting techniques, and discover our range of tools to help you reach your goals. 
- Credit Card Approval Detection
    - Discover our state-of-the-art credit card approval detection tool, which can help you make the necessary changes to your finance to be approved for a credit card.
"""
)