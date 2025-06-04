from embeddings.embedder import embed_query, find_closest_concepts

def retrieve_concepts(state):
    idea = state.get("divergent_expansion", "")
    query_vector = embed_query(idea)
    results = find_closest_concepts(query_vector, top_k=3)
    return {"concept_matches": results}
