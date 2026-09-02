import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Instruct-2507",
    task="text-generation",
    provider="nscale",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content='you are a helpful Ai assistant')
]

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Add user's message
    chat_history.append(
        HumanMessage(content=user_input)
    )

    # Send conversation history to model
    result = model.invoke(chat_history)

    # Add AI response to history
    chat_history.append(
        AIMessage(content=result.content)
    )

    print("AI:", result.content)

print(chat_history)
# it prints result
