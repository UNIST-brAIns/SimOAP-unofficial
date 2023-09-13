import math
import string

class TFIDF:
    def __init__(self, documents: list, ):
        self.documents = documents
        self.words = set()
        translator = str.maketrans('', '', string.punctuation)
        for doc in documents:
            print(doc)
            for word in doc.translate(translator).split():
                self.words.add(word)
        self.words = list(self.words)
            

    def TF(self, i, j):
        wordList = self.documents[j].split()
        return sum([1 if self.words[i]==wordList[k] else 0 for k in range(len(wordList))]) / (len(wordList))
    
    def IDF(self, i):
        return math.log(len(self.documents) / (1 + sum([1 if self.words[i] in self.documents[j].split() else 0 for j in range(len(self.documents))])), 2)
    
    def get_TFIDF(self, i, j):
        return self.TF(i, j) * self.IDF(i)
