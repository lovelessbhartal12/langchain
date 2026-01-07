import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",   # or gpt-4.1-mini
    temperature=0.7
)

responses = llm.batch([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
])
for response in responses:
    print(response)