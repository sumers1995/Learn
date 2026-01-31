from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "llama3.2:1b",
    temperature=0,
)

messages = [("system","You are a helpful assistant that translated Englist to French. Translate the user sentence."),
            ("human", "I love programming."),]

msg = llm.invoke(messages)
print(msg.content)