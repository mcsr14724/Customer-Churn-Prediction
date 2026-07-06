import streamlit as st
import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model


model=load_model('ann.keras')

with open('columntransformer.pkl', 'rb') as file:
    coltrans=pickle.load(file)

with open('standardscaler.pkl', 'rb') as file:
    stdscaler=pickle.load(file)

st.title('Churn Prediction')

CreditScore=st.number_input('CreditScore', min_value=0, max_value=1000, value=500)
Geography=st.selectbox('Geography', ['France', 'Spain', 'Germany'])
Gender=st.selectbox('Gender', ['Male', 'Female'])
Age=st.number_input('Age', min_value=0, max_value=100, value=30)
Tenure=st.number_input('Tenure', min_value=0, max_value=20, value=5)
Balance=st.number_input('Balance', min_value=0.0, max_value=1000000.0, value=10000.0)
NumOfProducts=st.number_input('Number of Products', min_value=0, max_value=10, value=1)
HasCrCard=st.selectbox('HasCrCard', [1,0])
IsActiveMember=st.selectbox('IsActiveMember', [1,0])
EstimatedSalary=st.number_input('Estimated Salary', min_value=0.0, max_value=1000000.0, value=50000.0)

input_data=pd.DataFrame({
    'CreditScore': [CreditScore],
    'Geography': [Geography],
    'Gender': [Gender],
    'Age': [Age],
    'Tenure': [Tenure],
    'Balance': [Balance],
    'NumOfProducts': [NumOfProducts],
    'HasCrCard': [HasCrCard],
    'IsActiveMember': [IsActiveMember],
    'EstimatedSalary': [EstimatedSalary]
})

input_data=coltrans.transform(input_data)
input_data=stdscaler.transform(input_data)

predict_prob=model.predict(input_data)[0][0]

if predict_prob>0.5:
    st.write('The customer is likely to churn with a probability of {:.2f}%'.format(predict_prob * 100))
else:
    st.write('The customer is not likely to churn with a probability of {:.2f}%'.format((1 - predict_prob) * 100))
