
import streamlit as st
from llm import create_chat, send_message

# Page configuration
st.set_page_config(
    page_title="AI Laptop Decision Assistant",
    page_icon="💻",
    layout="centered"
)

# Application title
st.title("💻 AI Laptop Assistant")
st.caption("Find the right laptop using AI reasoning and Python decision logic.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    try:
        st.session_state.chat = create_chat()
    except Exception as e:
        st.error(f"Gemini connection failed: {e}")
        st.stop()

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
user_input = st.chat_input(
    "Describe the laptop you are looking for..."
)

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Analyzing your requirements..."):

            try:
                response = send_message(
                    st.session_state.chat,
                    user_input
                )

                st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:

                error_message = f"Something went wrong: {e}"

                st.error(error_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })


# Clear conversation
if st.button("Clear Conversation"):

    st.session_state.messages = []
    st.session_state.chat = create_chat()

    st.rerun()



# Download conversation
if st.session_state.messages:

    conversation = ""

    for message in st.session_state.messages:

        role = message["role"].upper()

        conversation += f"\n{role}:\n"
        conversation += message["content"]
        conversation += "\n" + "-" * 40 + "\n"

    st.download_button(
        label="📥 Download Conversation",
        data=conversation,
        file_name="laptop_recommendation.txt",
        mime="text/plain"
    )
