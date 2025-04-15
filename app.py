import joblib
import streamlit as st
model = joblib.load('customer_segmentation')

if __name__ == '__main__':
    st.title('Customer Segmentation tool')
    X = st.number_input('Enter Annual Income: ')
    Y = st.number_input('Enter Spending Score: ')
    
    Z = st.button('Predict')

    if Z:
        A = model.predict([[X,Y]])
        if A == [0]:
            st.info('Customer with medium Annual Income and Spending')
        elif A == [1]:
            st.info('Customer with High Annual Income and Spending')
        elif A == [2]:
            st.info('Customer with Low Annual Income and High Spending')
        elif A == [3]:
            st.info('Customer with High Annual Income and Low Spending')
        elif A == [4]:
            st.info('Customer with Low Annual Income and Spending')



