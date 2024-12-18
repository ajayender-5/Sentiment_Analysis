import streamlit as st
import pandas as pd
import pickle

# Set page configuration to full width
st.set_page_config(page_title="Sentimental Analysis", page_icon="🏨")

# Load the trained model 
model = pickle.load(open("Prudent_Hackathon//logistic_regression1.pkl", "rb"))

# Function to predict sentiment
def predict_sentiment(review):
    prediction = model.predict([review])
    sentiment_map = {0: 'Negative😡', 2: 'Neutral😑', 1: 'Positive😊'}  # Adjust mapping based on your model
    return sentiment_map[prediction[0]]

# Streamlit app
def main():
    st.title(":rainbow[Trip Advisor Hotel Reviews]")
    st.write("Enter a hotel review and get the sentiment prediction.")

    # Input text box for the user to enter a review
    review = st.text_area("Enter the hotel review here:", "")

    # Predict sentiment button
    if st.button("Predict Sentiment"):
        if review:
            sentiment = predict_sentiment(review)
            st.write(f"Predicted Sentiment: {sentiment}")
        else:
            st.write("Please enter a review to predict its sentiment.")


if __name__ == "__main__":
    main()
