import streamlit as st
import numpy as np
import joblib

# model load
model = joblib.load("house_price_model.pkl")

# title
st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict the price")

# inputs
bedrooms = st.slider("Bedrooms", 1, 10, 2)
bathrooms = st.slider("Bathrooms", 1, 10, 1)
sqft_living = st.slider("Sqft Living", 500, 10000, 1500)

# button
if st.button("Predict Price"):

    # 57 features ka array banaya
    input_data = np.zeros((1,57))

    # first 3 features fill kiye
    input_data[0][0] = bedrooms
    input_data[0][1] = bathrooms
    input_data[0][2] = sqft_living

    # prediction
    prediction = model.predict(input_data)

    # result
    st.success(f"💰 Predicted Price: ${prediction[0]:,.2f}")