import streamlit as st
import joblib
import streamlit.components.v1 as components

# --- Load Model & Vectorizer ---
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# --- Load and render HTML frontend ---
with open("C:/Users/suraj/Downloads/EyeSpy/EyeSpy/frontend/index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Fullscreen responsive HTML
components.html(html_code, width="100%", height=2800, scrolling=False)  # height can be adjusted

# --- Streamlit Fake News Detection ---
st.write("---")
st.header("EyeSpy - Fake News Detector")

news_input = st.text_area("Enter the news article text here", height=300)

if st.button("Predict"):
    if news_input.strip():
        transformed_input = vectorizer.transform([news_input])
        prediction = model.predict(transformed_input)
        prediction_proba = model.predict_proba(transformed_input)

        if prediction[0] == 1:
            st.success(f"The news article is likely REAL with a confidence of {prediction_proba[0][1]*100:.2f}%")
        else:
            st.warning(f"The news article is likely FAKE with a confidence of {prediction_proba[0][0]*100:.2f}%")
    else:
        st.warning("Please enter some text to analyze.")