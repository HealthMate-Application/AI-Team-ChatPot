import streamlit as st
import requests


# Chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask your question:")

if st.button("Send") and user_input.strip() != "":
    try:
        # Get response from LLM chain
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": user_input}  # Changed to match API model
        )
        response.raise_for_status()  # Raise exception for bad status codes
        bot_reply = response.json().get("response", "No reply")
        
        # Save conversation history
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.chat_history.append(("Bot", bot_reply))
        
        # Clear input box
        user_input = ""
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with the server: {str(e)}")
        bot_reply = "Sorry, I encountered an error. Please try again."

# Display chat history
for speaker, text in st.session_state.chat_history:
    if speaker == "User":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")
