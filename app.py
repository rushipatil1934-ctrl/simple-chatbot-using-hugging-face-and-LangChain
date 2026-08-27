import os
import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


# Load environment variables
load_dotenv()


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🤖 AI Chatbot")
st.caption("Powered by LangChain + Hugging Face + Qwen")


# -----------------------------
# Create LLM
# -----------------------------
@st.cache_resource
def load_model():

    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen3-4B-Instruct-2507",
        task="text-generation",
        provider="nscale",
        huggingfacehub_api_token=os.getenv(
            "HUGGINGFACEHUB_API_TOKEN"
        )
    )

    return ChatHuggingFace(llm=llm)


model = load_model()


# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Ask me anything...")


if prompt:

    # -------------------------
    # Display User Message
    # -------------------------
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })


    # -------------------------
    # Create LangChain Messages
    # -------------------------
    chat_history = [
        SystemMessage(
            content="You are a helpful AI assistant. "
                    "Remember the previous conversation and "
                    "use it to answer the user's questions."
        )
    ]

    for message in st.session_state.messages:

        if message["role"] == "user":
            chat_history.append(
                HumanMessage(content=message["content"])
            )

        elif message["role"] == "assistant":
            chat_history.append(
                AIMessage(content=message["content"])
            )


    # -------------------------
    # Generate Response
    # -------------------------
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(chat_history)

            answer = response.content

        st.markdown(answer)


    # -------------------------
    # Save Assistant Response
    # -------------------------
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })