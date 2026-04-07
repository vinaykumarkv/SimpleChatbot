import streamlit as st
import backend as demo

st.title("Chat Bot")

#Initiate memory and chat history only once

if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

#Display messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

#Handle user input
input_text = st.chat_input("Use this Chatbot Powered By Gemini 2.5")
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    #get response
    response, updated_memory = demo.demo_conversation(
        input_text=input_text,
        memory=st.session_state.memory
    )
    st.session_state.memory = updated_memory

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "text": response})