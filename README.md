# 🤖 LangChain + Groq Chatbot

A simple, fast conversational chatbot built with **LangChain** and **Groq's** ultra-low-latency LLM inference, wrapped in a **Streamlit** chat UI and deployed on **Streamlit Cloud**.

**Live demo:** [https://pw4qjkvpihaykwntznotu8.streamlit.app/]

---

## Features

- Conversational chatbot with full chat history maintained across turns
- Powered by Groq's `openai/gpt-oss-20b` model for fast responses
- Clean chat interface built with Streamlit's native chat components
- "Clear chat" option to reset the conversation
- Secure API key handling — supports both local `.env` and Streamlit Cloud secrets
- Includes a standalone CLI version (`main.py`) for quick terminal-based testing

---

## Tech Stack

- [LangChain](https://www.langchain.com/) — orchestration of prompts, model calls, and output parsing
- [Groq](https://groq.com/) — LLM inference API
- [Streamlit](https://streamlit.io/) — web UI framework
- Python 3.10+

---

## Project Structure

```
├── app.py              # Streamlit web app (deployed version)
├── main.py             # CLI version of the chatbot
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## Running Locally

1. Clone the repo:
   ```bash
   https://github.com/saicharansamala-ai/-langchain-chatbot-groq.git
   cd langchain-chatbot-groq
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

   Or run the CLI version:
   ```bash
   python main.py
   ```

---

## Deployment

This app is deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). To deploy your own copy:

1. Push this repo to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io) and create a new app
3. Point it to `app.py` as the main file
4. Add `GROQ_API_KEY` under the app's **Secrets** settings
5. Deploy

---

## About This Project

Built as a hands-on project while transitioning into AI/GenAI engineering — exploring LLM orchestration with LangChain, third-party model APIs (Groq), and shipping a deployed, user-facing AI application end-to-end.

---

## License

MIT
