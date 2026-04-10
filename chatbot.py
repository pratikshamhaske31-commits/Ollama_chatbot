import streamlit as st
import requests

# Ollama API
OLLAMA_URL = "http://localhost:11434/api/generate"

st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖")

st.title("🤖 CREVA CHATBOT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to get response
def get_response(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": "phi",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

# Show chat history in UI
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input (BOTTOM like ChatGPT)
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_response(user_input)
            st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })