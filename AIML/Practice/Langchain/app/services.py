from langchain.agents import create_agent
# from langchain_core.messages import HumanMessage

agent = create_agent(
    model="ollama:qwen3:4b",
    system_prompt="You are a polymath and a professional."
)

def get_answer(query) -> str:
    result = agent.invoke({"messages": [{"role":"user", "content": query}]})
    return result["messsages"][-1].content