import google.generativeai as genai
import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def get_gemini_response(prompt):

    try:

        response = model.generate_content(prompt)

        print("Gemini response:")
        print(response.text)

        return response.text

    except Exception as e:

        print("Gemini Error:")
        print(e)

        return "Unable to generate response right now."
