from langchain_groq import ChatGroq

llm = ChatGroq(model="mixtral-8x7b-32768")

def evolve_idea(state):
    concepts = state.get("concept_matches", [])
    abstract_idea = state.get("divergent_expansion", "")
    top_concept = concepts[0]["concept"] if concepts else "a universal metaphor"

    prompt = f"""
Take the following abstract idea:
"{abstract_idea}"

And evolve it using the concept: "{top_concept}" into:
- A novel use case (scientific, business, social)
- A philosophical or poetic interpretation
- A high-level visual or symbolic metaphor

Be imaginative but coherent.
"""
    response = llm.invoke(prompt)
    return {"final_insight": response}
