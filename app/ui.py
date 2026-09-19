import streamlit as st

from app.agent import run_agent


st.set_page_config(
    page_title="Enterprise AI Operations Copilot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Enterprise AI Operations Copilot")
st.caption("RAG + Agentic AI assistant for enterprise operations")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input(
    "Ask about company policies or perform an IT operation..."
)


if user_input:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_agent(user_input)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )