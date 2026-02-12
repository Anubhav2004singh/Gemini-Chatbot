import os
import json

import streamlit as st

from openai import OpenAI
import google.generativeai as genai




GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")


st.set_page_config(
    page_title="AAO CHAT KARE",
    page_icon="╭∩╮(•̀_·́)╭∩╮",
    layout="centered"


)
#initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]



st.title("☠️ Anubhav Singh Chauhan SE BAAT KARLO")


for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



user_prompt=st.chat_input("Message Kar Lijiye Ankush Singh Chauhan")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    response = model.generate_content(user_prompt)


    assistant_response = response.text;


    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)