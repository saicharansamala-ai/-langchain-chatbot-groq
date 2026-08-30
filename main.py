
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load environment variables
load_dotenv()


# Create Groq model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)


# Output parser
parser = StrOutputParser()


def chat():
    chat_history = [
        ("system", "You are a helpful chatbot. Be concise and accurate.")
    ]

    print("LangChain Chatbot. Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            break

        # Add user message to history
        chat_history.append(("user", user_input))

        # Create prompt from complete conversation history
        prompt = ChatPromptTemplate.from_messages(chat_history)

        # Create LangChain chain
        chain = prompt | llm | parser

        # Get response
        response = chain.invoke({})

        print(f"Bot: {response}\n")

        # Add assistant response to history
        chat_history.append(("assistant", response))

        print("#" * 50)


if __name__ == "__main__":
    chat()
