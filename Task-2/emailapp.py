import streamlit as st
import pickle

# Load the saved model
model = pickle.load(open('spam.pickle', 'rb'))

# MAIN FUNCTION #

title = "Email Spam Classification App".upper()
st.markdown("<h1 style='text-align: center; font-size: 65px; color: #4682B4;'>{}</h1>".format(title),
            unsafe_allow_html=True)

info = ''

with st.expander("1. Check if your text is a spam or ham 😀"):
    text_message = st.text_input("Please enter your message")
    if st.button("Predict"):
        prediction = model.predict([text_message])[0]

        if prediction == 0:
            info = 'Not Spam'
            st.success('Prediction: {}'.format(info))
        else:
            info = 'Spam'
            st.error('Prediction: {}'.format(info))

# Pink color footer
st.markdown("<footer style='text-align: center; font-size: 20px; color: #FF69B4;'>Disha</footer>",
            unsafe_allow_html=True)
