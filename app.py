import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# 1. Setup and Visual Styling
load_dotenv()
st.set_page_config(page_title="Elderly Care Companion", layout="wide")

# Custom CSS for Lavender Background and senior readability
st.markdown("""
    <style>
    .stApp { background-color: #F3E5F5; } 
    h1, h2, h3 { color: #4A148C; }
    .stButton>button { 
        border-radius: 20px; 
        background-color: #7B1FA2; 
        color: white; 
        font-size: 20px !important; 
        height: 3em;
    }
    p, span, div { font-size: 22px !important; }
    </style>
    """, unsafe_allow_html=True) # Fixed the unsafe_allow_html error

st.title("👵 Elderly Voice Companion")

# 2. Sidebar for Groq API Key
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Enter Groq API Key", type="password")
    st.info("Get your free key at console.groq.com")

if api_key:
    client = Groq(api_key=api_key)
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.subheader("💬 Voice & Chat Support")
        if st.button("🎤 Tap to Speak"):
            st.info("Listening... (Simulating Voice Input)")
        
        if prompt := st.chat_input("How can I help you?"):
            # Emergency logic
            if any(word in prompt.lower() for word in ["help", "fall", "pain", "emergency"]):
                st.error("🚨 EMERGENCY ALERT! Notifying your family now.")
            
            # Using the latest supported Groq model
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[{"role": "system", "content": "You are a gentle assistant for seniors."},
                          {"role": "user", "content": prompt}]
            )
            st.write(res.choices[0].message.content)

    with col2:
        st.subheader("📋 Health Summary")
        notes = st.text_area("Paste doctor notes here:", height=200)
        if st.button("🔍 Simplify & Compress"):
            if notes:
                # Health Compression Logic
                comp_res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile", # Updated model name
                    messages=[{"role": "user", "content": f"Summarize this for a senior into 3 simple bullet points: {notes}"}]
                )
                st.success(comp_res.choices[0].message.content)
            else:
                st.warning("Please paste notes first.")
else:
    st.warning("👈 Please enter your Groq API Key to begin.")