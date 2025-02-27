# -*- coding: utf-8 -*-
"""Travel_options.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mWoxDZXGWkc5XAvGfeZ6esgDBKfynlBa
"""

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

GOOGLE_API_KEY = st.secrets.get('AIzaSyAZ01F26Iq4q9-P16ayZzv417pPdDK1x1c')

def get_travel_options(source, destination):
    system_prompt = SystemMessage(
        content="You are an AI-powered travel assistant. Provide multiple travel options (cab, train, bus, flight) with estimated costs, duration, and relevant travel tips."
    )
    user_prompt = HumanMessage(
        content=f"I am traveling from {source} to {destination}. Suggest travel options with estimated cost, duration, and important details."
    )

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY)

    try:
        response = llm.invoke([system_prompt, user_prompt])
        return response.content if response else "⚠️ No response from AI."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

# Streamlit UI
st.title("Travel Planner Assistant")
st.markdown("<h2 style='color: blue;'>Your Personal Travel Guide</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: green;'>Get the best travel options tailored just for you!</p>", unsafe_allow_html=True)

# Input fields for source and destination
source = st.text_input("Enter your source location:")
destination = st.text_input("Enter your destination location:")

# Button to fetch travel options
if st.button("Get Travel Options"):
    if source and destination:
        options = get_travel_options(source, destination)
        st.write(options)
    else:
        st.error("Please enter both source and destination.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h5 style='color: gray;'>Travel Planner made by Suman</h5>", unsafe_allow_html=True)
