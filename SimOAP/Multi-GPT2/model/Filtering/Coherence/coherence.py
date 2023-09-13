import sys
import os
sys.path.append(os.path.dirname(__file__))
import TFIDF
import numpy as np
def filter_coherence(history, candidates, c=5):
    tfidf = TFIDF.TFIDF([history] + candidates)
    reps = [[tfidf.get_TFIDF(i, j) for i in range(len(tfidf.words))] for j in range(1, len(tfidf.documents))]
    reps = np.array(reps)
    candidate_sim = [cos_sim(reps[:, 0], reps[:, j]) for j in range(1, len(tfidf.documents))]
    sorted_candidates = [x for _, x in sorted(zip(candidate_sim, candidates), key=lambda pair: pair[0])]
    candidates_index = [i for _, i in sorted(zip(candidate_sim, [ind for ind in range(len(candidates))]), key=lambda pair: pair[0])]

    return sorted_candidates[-c:], candidates_index[-c:]

def cos_sim(a, b):
    return (np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))).item()