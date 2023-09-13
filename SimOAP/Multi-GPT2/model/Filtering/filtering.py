import sys
import os
sys.path.append(os.path.dirname(__file__))
from Coherence.coherence import filter_coherence
from Consistency.consistency import filter_consistency

def filter(persona, history, candidates):
    candidates, indexes = filter_coherence(history, candidates)
    best, index = filter_consistency(persona, candidates, indexes)

    return best, index