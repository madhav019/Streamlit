import streamlit as st
import pandas as pd

st.title("Streamlit Demo")

st.header("Heading of Streamlit")

st.subheader("Sub-Heading of Streamlit")

st.text("Text of Streamlit")

st.success("Success")

st.warning("Warning")

st.info("Info")

st.error("Error")

if st.checkbox("Select / Unselect"):
    st.text("User selected the textbox")
else:
    st.text("User has not selected the textbox")

state = st.radio("What is ypur favorite color", ("Red", "Green", "Yellow"))

st.selectbox("What do you do ?", ['Student', "Vlogger", "Engineer"])

st.button("Submit")

st.table(pd.DataFrame({"Name": ['Madhav', "Chawla"], "Age": [10, 23]}))

st.sidebar.header("Madhav's App")

st.text("Loan prediction")