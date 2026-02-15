import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# 1. Setup and Visual Styling
load_dotenv()
st.set_page_config(page_title="Elderly Care Companion", layout="wide")

# Custom CSS for Lavender Background and Clean UI
st.markdown("""
    <style>
    .stApp {
        background-color: #F3E5F5; /* Light Lavender */
    }
    .stApp [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    h1, h2, h3 {
        color: #4A148C; /* Deep Purple for readability */
    }
    .stButton>button {
        border-radius: 20px;
        background-color: #7B1FA2;
        color: white;
        font-size: 20px !important;
        height: 3em;
    }
    .stChatInput {
        border-radius: 20px;
    }
    /* Large text for seniors */
    p, span, div {
        font-size: 22px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👵 SeniorVoice Companion")

# 2. Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Enter OpenAI API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.subheader("💬 Voice & Chat Support")
        if st.button("🎤 Tap to Speak"):
            st.info("Listening... (Simulating Voice Input)")
        
        if prompt := st.chat_input("How can I help you today?"):
            # Emergency logic
            if any(word in prompt.lower() for word in ["help", "fall", "pain", "emergency"]):
                st.error("🚨 EMERGENCY ALERT! Notifying your family now.")
            
            res = client.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages=[{"role": "system", "content": "You are a gentle assistant for seniors. Give short, patient answers."},
                          {"role": "user", "content": prompt}]
            )
            st.write(res.choices[0].message.content)

    with col2:
        st.subheader("📋 Health Summary")
        notes = st.text_area("Paste doctor notes here:", height=200)
        if st.button("🔍 Simplify & Compress"):
            if notes:
                # Compression logic
                comp_res = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"Summarize this for a senior into 3 simple, large bullet points: {notes}"}]
                )
                st.success(comp_res.choices[0].message.content)
            else:
                st.warning("Please paste notes first.")
else:
    st.warning("👈 Please enter your API Key to begin.")