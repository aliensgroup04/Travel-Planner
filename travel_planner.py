# -*- coding: utf-8 -*-
"""Travel_planner.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aCQyry45GnQGD7un_dJEybLvVhP5E3hr
"""
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.chat_models import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

# Load API key from .env file (recommended)
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Ensure API key is set
if not api_key:
    st.error("Google API key is missing! Set it in a .env file or as an environment variable.")
else:
    os.environ["GOOGLE_API_KEY"] = api_key

# Initialize the AI model
model = ChatGoogleGenerativeAI(model="gemini-pro")

def get_travel_recommendations(source, destination):
    """Fetch travel recommendations using Google GenAI."""
    prompt = f"Suggest travel options from {source} to {destination} with estimated costs (cab, train, bus, flights)."
    response = model([HumanMessage(content=prompt)])
    return response.content if response else "No response from AI."

# Streamlit UI
st.title("🚀 AI-Powered Travel Planner")
st.markdown("Enter your source and destination to get travel options.")

source = st.text_input("Source", placeholder="Enter starting location")
destination = st.text_input("Destination", placeholder="Enter destination")

if st.button("Find Travel Options"):
    if source and destination:
        st.write("🔎 Fetching travel recommendations...")
        recommendations = get_travel_recommendations(source, destination)
        st.write(recommendations)
    else:
        st.warning("⚠️ Please enter both source and destination.")


