from prompts import load_prompt
from langchain_groq import ChatGroq

# You could swap ChatGroq with another LLM provider (e.g., OpenAI or Anthropic's Claude).
llm = ChatGroq(model="mixtral-8x7b-32768")

def generate_thought_seeds(state):
    user_input = state["user_input"]
    prompt_template = load_prompt("thought_seeds")
    prompt = prompt_template.replace("{{user_input}}", user_input)
    response = llm.invoke(prompt)
    return {"thought_seeds": response}
