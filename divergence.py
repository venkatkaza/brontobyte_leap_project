from config.prompts import load_prompt
from langchain_groq import ChatGroq

llm = ChatGroq(model="mixtral-8x7b-32768")

def expand_divergence(state):
    seeds = state.get("thought_seeds", "")
    prompt_template = load_prompt("divergence")
    prompt = prompt_template.replace("{{seed}}", seeds)
    response = llm.invoke(prompt)
    return {"divergent_expansion": response}
