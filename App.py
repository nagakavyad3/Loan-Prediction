import streamlit as st
import pandas as pd
import pickle as pk

model = pk.load(open('model (1).pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))


st.title('Loan Predcition App')

no_of_dep = st.text_input('Choose No of dependents', 0, 5)
grad = st.selectbox('Choose Education',['Graduated','Not Graduated'])
self_emp = st.selectbox('Self Emoployed ?',['Yes','No'])
Annual_Income = st.text_input('Choose Annual Income', 0, 10000000)
#st.warning("please enter numbers ")

Loan_Amount = st.text_input('Choose Loan Amount', 0, 10000000)
Loan_Dur = st.text_input('Choose Loan Duration', 0, 20)
Cibil = st.text_input('Choose Cibil Score', 0, 1000)
Assets = st.text_input('Choose Assets', 0, 10000000)

if grad =='Graduated':
    grad_s =0
else:
    grad_s = 1

if self_emp =='No':
    emp_s =0
else:
    emp_s = 1

if st.button("Predict"):
    pred_data = pd.DataFrame([[no_of_dep,grad_s,emp_s,Annual_Income,Loan_Amount,Loan_Dur,Cibil,Assets]],
                         columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Assets'])
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Loan Is Approved')
    else:
        st.markdown('Loan Is Rejected')
