import streamlit as st
import requests
import codecs


st.set_page_config(page_title="Groq Chat", page_icon="🤖", layout="centered")
st.title("🤖 Chat with Groq LLM (Streamed)")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user's message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Placeholder for streamed assistant response
    with st.chat_message("assistant"):
        streamed_text = ""
        container = st.empty()

        # Call your FastAPI endpoint with stream
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            params={"message": prompt}
        )

        decoder = codecs.getincrementaldecoder("utf-8")()
        streamed_text = ""
        container = st.empty()

        for chunk in response.iter_content(chunk_size=1):
            if chunk:
                streamed_text += decoder.decode(chunk)
                container.markdown(streamed_text + "▌")  # Typing cursor

        # Flush any remaining buffered characters
        streamed_text += decoder.decode(b"", final=True)
        container.markdown(streamed_text)  # Final display

        # Append assistant response to session history
        st.session_state.messages.append({"role": "assistant", "content": streamed_text})
