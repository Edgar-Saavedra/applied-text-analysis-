from numpy import vectorize
from sklearn.feature_extraction.text import CountVectorizer
from BagOfWords import corpus

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(corpus)

print(vectors)