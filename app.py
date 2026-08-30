import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables (for local dev; Streamlit Cloud uses st.secrets)
load_dotenv()

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 LangChain + Groq Chatbot")
st.caption("Powered by openai/gpt-oss-20b via Groq")

# --- Get API key: works both locally (.env) and on Streamlit Cloud (secrets) ---
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", None)

if not groq_api_key:
    st.error("GROQ_API_KEY not found. Add it to your .env file (local) or Streamlit Cloud Secrets.")
    st.stop()

# --- Cache the model so it isn't recreated on every rerun ---
@st.cache_resource
def get_llm():
    return ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.2,
        groq_api_key=groq_api_key,
    )

llm = get_llm()
parser = StrOutputParser()

# --- Initialize chat history in session state ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("system", "You are a helpful chatbot. Be concise and accurate.")
    ]

# --- Sidebar controls ---
with st.sidebar:
    st.header("Settings")
    if st.button("🗑️ Clear chat"):
        st.session_state.chat_history = [
            ("system", "You are a helpful chatbot. Be concise and accurate.")
        ]
        st.rerun()

# --- Render existing chat history (skip system message) ---
for role, content in st.session_state.chat_history:
    if role == "system":
        continue
    with st.chat_message(role):
        st.markdown(content)

# --- Chat input ---
user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.chat_history.append(("user", user_input))

    prompt = ChatPromptTemplate.from_messages(st.session_state.chat_history)
    chain = prompt | llm | parser

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke({})
        st.markdown(response)

    st.session_state.chat_history.append(("assistant", response))