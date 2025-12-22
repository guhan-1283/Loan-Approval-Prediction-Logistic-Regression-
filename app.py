import streamlit as st
import joblib 
import numpy as np


model = joblib.load("model.pkl")
scaler  =joblib.load("scaler.pkl")   

st.image("loan.png", caption="Loan Approval System",width=200)
st.title("Loan Approval System")


st.divider()


gender_dict = {
    "Male": 0,
    "Female": 1
}

gender_label = st.selectbox(
    "Gender",
    ["Gender"] + list(gender_dict.keys())
)

if gender_label == "Gender":
    gender = None
else:
    gender = gender_dict[gender_label]


married_dict = {
    "Yes":0,
    "No":1
}

married_label = st.selectbox("Married",["Married or not"]+list(married_dict.keys()))

if married_label == "Married or not":
    married = None
else:
    married = married_dict[married_label]



Dependents = st.number_input("Enter the dependents",min_value=1,step=1)


education_dict = {
    "Graduate":0,
    "Non Graduate":1
}

education_label = st.selectbox("Education",["Education"]+list(education_dict.keys()))

if education_label == "Education":
    education = None
else:
    education = education_dict[education_label]



self_employed_dict = {
    "Yes":0,
    "No":1
}

self_employed_label = st.selectbox("Self Employed",["Self Employed or not"]+list(self_employed_dict.keys()))

if self_employed_label == "Self Employed or not":
    self_employed = None
else:
    self_employed = self_employed_dict[self_employed_label]



applicant_income = st.number_input("Enter the Applicant Income")
coapplicant_income = st.number_input("Enter the CoApplicant Income")
loan_amount = st.number_input("Enter the Loan amount")
loan_amount_term = st.number_input("Enter the Loan amoun Term")


credit_history = st.number_input("Enter the Credit History",min_value=0.0,max_value=1.0,step=1.0)


property_area_dict = {
    "Semi Urban":0,
    "Urban":2,
    "Rural":1
}

property_area_label = st.selectbox("Property Area",["Property Area"]+list(property_area_dict.keys()))

if property_area_label == "Property Area":
    property_area = None
else:
    property_area = property_area_dict[property_area_label]



X = [gender,married,Dependents,education,self_employed,applicant_income,coapplicant_income,loan_amount,
     loan_amount_term,credit_history,property_area]



st.divider()


predict = st.button("Predict this button for checking Loan Approval")



if predict:
    st.snow()

    X1 =  np.array([X])

    scaled_data = scaler.transform(X1)
    prediction = model.predict(scaled_data)

    if prediction == 0:
        st.write("The Loan has been approved")
    elif prediction == 1:
        st.write("The Loan is not approved")

else:
    "Please press the Predict Button for Prediction"
