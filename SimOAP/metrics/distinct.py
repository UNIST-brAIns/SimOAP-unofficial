import string

def distinct(sentence, ngram):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = sentence.translate(translator)
    # Split the cleaned text into a list of words
    word_list = cleaned_text.split()

    distinct_ngram = set()
    count = 0

    for i in range(len(word_list) - ngram + 1):
        ngram = " ".join(word_list[i : (i + ngram)])
        count += 1
        distinct_ngram.add(ngram)
    
    return len(distinct_ngram) / count