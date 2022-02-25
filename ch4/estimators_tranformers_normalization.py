# The root of of interfaces in Scikit-Learn is an Estimator
# Primary Estimator objects implement classifiers, regressor or clustering algorithms
# can in clued manipulation (dimensionality reduction, feature extraction)

# Estimator serves as an interface. Classes that implement it must have 2 methods:
# fit and predict

from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
  # Estimator.fit sets the state of the estimator based on the training data.
  # trainingData is expected to be matrix-like. Example: 2-d Numpy array of shape (n_samples, n_features)
  # or Pandas DataFrame (rows - instances, columns - features)

  # y - one-dimensional that holds the correct labels
  # fitting modifies  the internal state of the estimator such that it is ready or able to make predictions.

  # the state is saved in Estimator.coefs_
  def fit(self, trainingData, y=None):
    """
    Accept input data, X and optinal target data, y. Returns self.
    """
    return self

  # Estimator.predict creates predictions using the internal fitted state on new data 
  # the input must have the smae number of columns as the training data passed to fit.
  # yhat is a vector that contains the predictions for each row
  def predict(self, newData):
    """
    Accept input data, newData and return a vector of predictions for each row.
    """
    return yhat

# Estimator has parameters that define how the fitting process is conducted
# The parameters are set when instanciated
# can be modified with get_param and set_param

def estimator_naive_bayes(documents, labels):
  from sklearn.naive_bayes import MultinomialNB

  # alpha - used for additive smoothing
  # class_prior - prior probabiliteis for each of our 2 classes.
  model = MultinomialNB(alpha=0.0, class_prior=[0.4, 0.6])
  model.fit(documents, labels)

# Transformer interface.
# A transformer is a special type of Estimator that creates a new dataset from
# an old one based on rules that it has learned from the fitting process
from sklearn.base import TransformerMixin

class Transformer(BaseEstimator, TransformerMixin):
  def fit(self, trainingData, labels=None):
    """
    Learn how to transform data based on input data X.
    """
    return self

  # takes a dataset and returns a new dataset with new labels
  # transformers in Scikit-Learn are used to normalize/scale features, 
  # handle missing values, perform dimensionality reduction, extract/select features
  # perform mappings from on feature space to another
  def transform(self, newData):
    """
    Transform newData in a new dataset (xprime) and return it
    """
    return Xprime

# gensim vectorization are great. Can be loaded from disk to remain decoupled from pipeline
# Possible to build tranformer that uses Gensim vectorization

import os
from gensim.corpora import Dictionary
from gensim.matutils import sparse2full

class GensimVectorizer(BaseEstimator, TransformerMixin):
  def __init__(self, path=None):
    self.path = path
    self.id2word = None
    self.load()

  def load(self):
    if os.path.exists(self.path):
      self.id2word = Dictionary.load(self.path)
  
  # allows to save dictionary to disk
  def save(self):
    self.id2word.save(self.path)
  
  # Wraps a gensim Dictionary generated during fit
  # Constructs the Dictionary by passing already tokenized
  # and normalized documents to the Dictionary
  def fit(self, documents, labels=None):
    self.id2word = Dictionary(documents)
    self.save()
    return self

  # the dictionary can be can be saved an loaded from dis.
  # doc2bow retusn a sparse representation fo the document as  list (token_id, frequency) tuples
  # sparse2full to convert sparse to a nympy array
  def transform(self, documents):
    for document in documents:
      docdev = self.id2word.doc2bow(document)
      yield sparse2full(docdev, len(self.id2word))

# as feature space increase in dmension, data becomes more sparse and less informative
# text normalization reduces number of dimensions
# text normalization does stemming and lemmatization

# Stemming - series of rules to slice a string to a smaller stubstring. Remove affices
# Lemmatization - uses a dictionary to lookup every token and returns the "head" word called a Lemma
# Lemma example: 'gardening' -> 'to garden' , 'garden' and 'gardener' different Lemma 

# This uses NLTK very heavily
# other options:
# - remove tokens that appera above or below a particular count threshold
# - removing stopwords, only selecting the first five to 10 thousand
# - computing the cumulative frequency and only selecting words that contain 10%-50% of the cumulative frequency
# an alternative approca is to perform dimensionality reductions with
# PCA (Principal Component Analysis) or Singular Value Decomposition (SVD)
import unicodedata
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn

class TextNormalizer(BaseEstimator, TransformerMixin):

  # langauge used to load correct stopwords from NLTK corpus

  def __init__(self, language='english'):
    self.stopwords = set(nltk.corpus.stopwords.words(language))
    self.lemmatizer = WordNetLemmatizer()

  # checks if every char is the token and has unicode category that starts with 'P' (punctuation)
  def is_punct(self, token):
    return all(
      unicodedata.category(char).startswith('P') for char in token
    )
  
  # determines if the token is in our set of stopwords
  def is_stopword(self, token):
    return token.lower() in self.stopwords
  
  # takes single doc (token, tag) tuples
  def normalize(self, document):
    return [
      self.lemmatize(token, tag).lower()
      for paragraph in document
      for sentence in paragraph
      for (token, tag) in sentence
      if not self.is_punct(token) and not self.is_stopword(token)
    ]

  # applies the filtering functions to remove unwanted tokens and then lemmatizes them. Converts
  # Penn Treebank part-of-speech tags that are default tag set in the nltk.pos_tag function to WordNet tags
  def lemmatize(self, token, pos_tag):
    tag = {
      'N': wn.NOUN, 
      'V': wn.VERB,
      'R': wn.ADV,
      'J': wn.ADJ
    }.get(pos_tag[0], wn.NOUN)

    return self.lemmatizer.lemmatize(token, tag)


  def fit(self, X, y=None):
    return self

  def transform(self, documents):
    for document in documents
      yield self.normalize(document)