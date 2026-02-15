import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="Elderly Care Companion", layout="wide")

# Senior-friendly styling
st.markdown("""
    <style>
    .stApp { background-color: #F3E5F5; } 
    h1, h2, h3 { color: #4A148C; }
    .stButton>button { border-radius: 20px; background-color: #7B1FA2; color: white; font-size: 20px !important; height: 3em; }
    p, span, div { font-size: 22px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("👵 SeniorVoice Companion")

with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Enter Groq API Key", type="password")
    # NEW: Language Selector
    target_lang = st.selectbox("Select Your Language", ["English", "Hindi", "Spanish", "French", "German"])
    st.info("The AI will respond in your chosen language.")

if api_key:
    client = Groq(api_key=api_key)
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.subheader("💬 Voice & Chat Support")
        if prompt := st.chat_input("How can I help you?"):
            if any(word in prompt.lower() for word in ["help", "fall", "pain", "emergency"]):
                st.error("🚨 EMERGENCY ALERT! Notifying your family now.")
            
            # Updated Prompt for Multilingual Support
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[{"role": "system", "content": f"You are a gentle assistant for seniors. Always respond in {target_lang}."},
                          {"role": "user", "content": prompt}]
            )
            st.write(res.choices[0].message.content)

    with col2:
        st.subheader("📋 Health Summary")
        notes = st.text_area("Paste doctor notes here:", height=200)
        if st.button("🔍 Simplify & Compress"):
            if notes:
                # Updated Logic: Summarize AND Translate
                comp_res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": f"Summarize these notes into 3 simple bullet points. The final output MUST be in {target_lang}: {notes}"}]
                )
                st.success(comp_res.choices[0].message.content)
else:
    st.warning("👈 Please enter your Groq API Key and select a language.")