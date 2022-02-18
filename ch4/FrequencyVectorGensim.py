from locale import normalize
from BagOfWords import corpus
from BagOfWords import tokenize
# from sklearn.feature_extraction.text import TfidfVectorizer

import gensim


# TermFrequency-Inverse
# Bag of words does not take into account context
# normalizes the frequency of tokens in a document with respect to the rest of corpus
# accentuate terms that are very relevant to a specific instance

# we first construct the lexicon and use it to instantiate the TFidModel
# The TfidfModle computes the normalized inverse document frequency
# we can then fetch the TF-IDF reqpresentation for each vector using getitem
corpus = [tokenize(doc) for doc in corpus]
lexicon = gensim.corpora.Dictionary(corpus)
tfidf = gensim.models.TfidfModel(dictionary=lexicon, normalize=True)
vectors = [tfidf[lexicon.doc2bow(doc)] for doc in corpus]

# to save a Gensim model to disk
lexicon.save_as_text('/Users/esaavedra/Work/personal/projects/applied-text-analysis/ch4/lexicon.txt', sort_by_word=True)
tfidf.save('/Users/esaavedra/Work/personal/projects/applied-text-analysis/ch4/tfidf.pkl')

# to load the model from disk
# lexicon = gensim.corpora.Dictionary.load_from_text('/Users/esaavedra/Work/personal/projects/applied-text-analysis/ch4/lexcon.txt')
# tfidf = gensim.models.TfidfModel.load('tfidf.pkl')