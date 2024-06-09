import streamlit as st
from testPredict import testPredictFunc

st.write("# Stock Price Prediction")

with st.form("prediction_form"):
    st.write("## Interactive stock price prediction form - click Submit to run prediction")
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write(f"## You're running now a prediction for your stock!")
        st.write("## This is your result: ")
        st.write(testPredictFunc())