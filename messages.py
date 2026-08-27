import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

##llm = HuggingFaceEndpoint(
  ##  repo_id="Qwen/Qwen3-4B-Instruct-2507",
   ## task="text-generation",
   ## provider="nscale",
    ##huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
##)

model = ChatHuggingFace()


messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What is Python?")
]

result = model.invoke(messages)

print(messages)