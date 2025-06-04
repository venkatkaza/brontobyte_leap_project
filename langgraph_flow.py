from langgraph.graph import StateGraph
from nodes.thought_seeds import generate_thought_seeds
from nodes.divergence import expand_divergence
from nodes.concept_retrieval import retrieve_concepts
from nodes.evolution import evolve_idea

workflow = StateGraph()
workflow.add_node("thought_seeds", generate_thought_seeds)
workflow.add_node("divergence", expand_divergence)
workflow.add_node("concepts", retrieve_concepts)
workflow.add_node("evolve", evolve_idea)

workflow.set_entry_point("thought_seeds")
workflow.add_edge("thought_seeds", "divergence")
workflow.add_edge("divergence", "concepts")
workflow.add_edge("concepts", "evolve")
workflow.set_finish_point("evolve")

app_flow = workflow.compile()
def run_concept_leap(prompt):
    return app_flow.invoke({"user_input": prompt})