import streamlit as st
import pickle
import numpy as np

# Load the saved loan default prediction model
loan_default_model = pickle.load(open('loan_default_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox("Loan Default Prediction System", ['Loan Default Prediction'])

# Loan Default Prediction Page
if selected == 'Loan Default Prediction':

    # Page title
    st.title('Loan Default Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Client_Income = st.text_input('Client Income')
        House_Own = st.text_input('House Ownership (1 for Yes, 0 for No)')
        Credit_Amount = st.text_input('Credit Amount')
        Accompany_Client = st.text_input('Accompany Client')
        Population_Region_Relative = st.text_input('Population Region Relative')

    with col2:
        Active_Loan = st.text_input('Active Loan (1 for Yes, 0 for No)')
        Loan_Annuity = st.text_input('Loan Annuity')
        Client_Income_Type = st.text_input('Client Income Type (Numeric Encoding)')
        Client_Marital_Status = st.text_input('Client Marital Status (Numeric Encoding)')
        Age_Days = st.text_input('Age (in Days)')

    with col3:
        Employed_Days = st.text_input('Days Employed')
        ID_Days = st.text_input('ID Days')
        Mobile_Tag = st.text_input('Mobile Tag (1 for Yes, 0 for No)')
        Client_Occupation = st.text_input('Client Occupation (Numeric Encoding)')
        Client_Family_Members = st.text_input('Number of Family Members')

    col4, col5 = st.columns(2)

    with col4:
        Cleint_City_Rating = st.text_input('Client City Rating (1 to 3)')
        Client_Permanent_Match_Tag = st.text_input('Permanent Match Tag (1 for Yes, 0 for No)')
        Social_Circle_Default = st.text_input('Social Circle Default')

    with col5:
        Credit_Bureau = st.text_input('Credit Bureau Score')

    # Code for Prediction
    loan_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Check Loan Default Risk'):
        try:
            # Prepare the input data as an array
            input_data = np.array([[float(Client_Income), int(Active_Loan), int(House_Own), float(Credit_Amount), float(Loan_Annuity), 
                                    int(Accompany_Client), int(Client_Income_Type), int(Client_Marital_Status), float(Population_Region_Relative), 
                                    int(Age_Days), int(Employed_Days), int(ID_Days), int(Mobile_Tag), int(Client_Occupation), 
                                    int(Client_Family_Members), int(Cleint_City_Rating), int(Client_Permanent_Match_Tag), 
                                    int(Social_Circle_Default), float(Credit_Bureau)]])

            # Make prediction using the model
            loan_prediction = loan_default_model.predict(input_data)
            
            # Display result
            if loan_prediction[0] == 1:
                loan_diagnosis = 'The client is likely to default on the loan.'
            else:
                loan_diagnosis = 'The client is not likely to default on the loan.'
            
            st.success(loan_diagnosis)
        
        except Exception as e:
            st.error(f"Error occurred: {e}")

