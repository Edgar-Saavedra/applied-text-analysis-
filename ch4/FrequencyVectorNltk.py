from collections import defaultdict
from BagOfWords import tokenize
from BagOfWords import corpus

def vectorize(doc):
  features = defaultdict(int)
  for token in tokenize(doc):
    features[token] += 1

  return features

vectors = map(vectorize, corpus)
print(vectors)