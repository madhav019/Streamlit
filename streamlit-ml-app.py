import joblib
import streamlit as st
import numpy as np

model_name = "RF_Loan_model.joblib"
model = joblib.load(model_name)


def prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):
    
    Gender = 1 if Gender == "Male" else 0
    
    Married = 1 if Married == "Yes" else 0
    
    Education = 1 if Education == "Not Graduate" else 0
    
    Self_Employed = 1 if Self_Employed == "Yes" else 0
    
    TotalIncome = np.log(ApplicantIncome + CoapplicantIncome)
    
    Credit_History = 1 if Credit_History == "Outstanding Loan" else 0
    
    Property_Area = 0 if Property_Area == "Rural" else 1 if Property_Area == "Semi Urban" else 2
    
    prediction = model.predict([[Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, TotalIncome]])
    
    print(prediction)
    
    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Approved"
        
    return pred



def main():
    st.title("Welcome to loan application")
    st.header("Please enter your details to proceed with the loan application")
    
    Gender = st.selectbox("Gender", ["Male", "Female"])
    
    Married = st.selectbox("Married", ["Yes", "No"])
    
    Dependents = st.number_input("Number of Dependents")
    
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
    
    ApplicantIncome = st.number_input("Applicant Income")
    
    CoapplicantIncome = st.number_input("Co-applicant Income")
    
    LoanAmount = st.number_input("Loan Amount")
    
    Loan_Amount_Term = st.number_input("Loan Amount Term")
    
    Credit_History = st.selectbox("Credit_History", ["Outstanding Loan", "No Outstanding Loan"])
    
    Property_Area = st.selectbox("Property Area", ["Rural", "Urban", "Semiurban"])
    
    
    if st.button("Predict"):
        result = prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)
        
        if(result == "Approved"):
            st.success("Your loan application is Approved!")
        else:
            st.error("Your loan application is Rejected!")
    
    
if __name__ == "__main__":
    main()