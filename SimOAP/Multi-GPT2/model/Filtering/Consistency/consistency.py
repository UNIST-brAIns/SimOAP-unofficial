from transformers import TextClassificationPipeline
from transformers import RobertaTokenizer, RobertaForSequenceClassification
def filter_consistency(persona, candidates, candidates_index):
    # Use a pipeline as a high-level helper
    tokenizer = RobertaTokenizer.from_pretrained("roberta-large-mnli")
    model = RobertaForSequenceClassification.from_pretrained("roberta-large-mnli", num_labels=3)
    classifier = TextClassificationPipeline(model, tokenizer)
    entailment = []
    for i in range(len(candidates)):
        entailment.append(classifier(persona + candidates[i])[0]["score"])
    
    sorted_candidates = [x for _, x in sorted(zip(entailment, candidates), key=lambda pair: pair[0])]
    candidates_index = [i for _, i in sorted(zip(entailment, candidates_index), key=lambda pair: pair[0])]
    return sorted_candidates[-1], candidates_index[-1]