diff --git a//dev/null b/embeddings/embedder.py
index 0000000000000000000000000000000000000000..00c6afc825fc1b651abd84b24c32d4af47c22b2d 100644
--- a//dev/null
+++ b/embeddings/embedder.py
@@ -0,0 +1,42 @@
+import json
+import numpy as np
+from pathlib import Path
+
+VECTOR_STORE_PATH = Path(__file__).resolve().parent.parent / "vector_store.json"
+
+
+def _load_vectors():
+    with open(VECTOR_STORE_PATH, "r") as f:
+        return json.load(f)
+
+
+VECTOR_STORE = _load_vectors()
+
+
+def _hash_text(text: str, dims: int = 5) -> np.ndarray:
+    """Create a deterministic pseudo-embedding for the given text."""
+    import hashlib
+    h = hashlib.sha256(text.encode("utf-8")).digest()
+    # Convert bytes to floats between -1 and 1
+    ints = np.frombuffer(h, dtype=np.uint8)[:dims]
+    return (ints / 255.0) * 2 - 1
+
+
+def embed_query(text: str) -> np.ndarray:
+    return _hash_text(text)
+
+
+def find_closest_concepts(query_vector: np.ndarray, top_k: int = 3):
+    def distance(vec):
+        vec = np.array(vec)
+        return np.linalg.norm(query_vector - vec)
+
+    scored = [
+        (distance(item["vector"]), item["concept"])
+        for item in VECTOR_STORE
+    ]
+    scored.sort(key=lambda x: x[0])
+    return [
+        {"concept": concept, "distance": dist}
+        for dist, concept in scored[:top_k]
+    ]
