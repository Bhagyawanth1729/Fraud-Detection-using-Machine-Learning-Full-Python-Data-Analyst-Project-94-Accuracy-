import streanlit as st
import pandas as pd
import joblib

model=jolib.load(r"C:\Users\bhagyawanth\OneDrive\Desktop\place_ment\Data analyast\Python Project For Data Analysis- Exploratory Data Analysis (EDA)\Fraud detection\Fraud_detection_pipeline.pkl")

st.title("fraud Detection Prediction App")

st.markdown("Please enter the  transaction details and use the predict button")
 st.divider()

transaction_type=st.selectbox("Tranaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT")
amount=st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input("Old Balance (sender)",min_values=0.0,values=10000.0)
newbalanceOrig=st.number_input("New Balance (sender)",min_values=0.0,values=9000.0)
oldbalanceDest=st.number_input("Old Balance  (Receiver)",min_values=0.0,values=0.0)
newbalanceDest=st.number_input("Old Balance  (Receiver)",min_values=0.0,values=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame(({
        "type": transaction_type,                 # or "transaction_type" if you prefer the exact name
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }))
    prediction=model.predict(input_data)[0]

    st.subheader(f"prediction:'{int(prediction)}'")

    if prediction ==1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")
    