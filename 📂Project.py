import streamlit as st

st.title("📂 My Project")

project = {"E-Attendance Navigator": "📊 Attendance system with report.", "SAOD Web App": "🛒 Promotes local products.", "Banking System": "🏦 Handles transactions and analytics."}

for name, desc in project.items() :
    with st.expander(name) :
        st.write(desc)