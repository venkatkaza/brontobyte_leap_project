from prompts import load_prompt
from langchain_groq import ChatGroq

llm = ChatGroq(model="mixtral-8x7b-32768")  # You can also use OpenAI, Claude etc.

def generate_thought_seeds(state):
    user_input = state["user_input"]
    prompt_template = load_prompt("thought_seeds")
    prompt = prompt_template.replace("{{user_input}}", user_input)
    response = llm.invoke(prompt)
    return {"thought_seeds": response}
