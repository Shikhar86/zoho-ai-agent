from langchain_ollama import ChatOllama

json_llm = ChatOllama(
    model="llama3",
    temperature=0,
    format="json"
)

text_llm = ChatOllama(
    model="llama3",
    temperature=0
)