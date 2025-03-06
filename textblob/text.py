import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive 😊"
    elif sentiment < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Streamlit UI
st.title("Sentiment Analysis App")
st.write("Enter text below to analyze its sentiment.")

user_input = st.text_area("Enter your text:")

if st.button("Analyze"):
    if user_input:
        sentiment_result = analyze_sentiment(user_input)
        st.subheader("Sentiment Result:")
        st.write(sentiment_result)
    else:
        st.warning("Please enter some text to analyze.")
