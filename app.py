import streamlit as st
from langgraph_flow import run_concept_leap

st.title("🧠 Brontobyte Leap: Cognitive Leap Engine")
user_prompt = st.text_area("Enter your idea, question, or thought:")
if st.button("Generate Abstract Leap"):
    with st.spinner("Generating insights..."):
        output = run_concept_leap(user_prompt)
        st.subheader("🌌 Cognitive Leap Result")
        st.write(output.get("final_insight", "No result"))