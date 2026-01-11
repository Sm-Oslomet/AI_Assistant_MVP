

from typing import List, Dict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SIMILARITY_THRESHOLD = 0.35  # conservative, tune later


class SemanticRetriever:
    def __init__(self, fragments: List[Dict]):
        self.fragments = fragments
        self.texts = [f["text"] for f in fragments]

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )

        self.fragment_vectors = self.vectorizer.fit_transform(self.texts)

    def retrieve(self, question: str) -> List[Dict]:
        question_vector = self.vectorizer.transform([question])
        similarities = cosine_similarity(
            question_vector, self.fragment_vectors
        )[0]

        results = []
        for fragment, score in zip(self.fragments, similarities):
            if score >= SIMILARITY_THRESHOLD:
                hit = fragment.copy()
                hit["similarity"] = float(score)
                results.append(hit)

        results.sort(key=lambda x: x["similarity"], reverse=True)
        return results
