import nltk
import string

from numpy import vectorize

# The corpus object
corpus = [
    "The elephant sneezed at the sight of potatoes.",
    "Bats can see via echolocation. See the bat sight sneeze!",
    "Wondering, she opened the door to the studio.",
]

# bag-of-words exmpale. Every doc is a vector, with length equal to the vocab.

# tokenize performs ligthweight normalization
#   - stripping punctuation using string.punctuation
#   - set text to lower case
#   - remove affixes "bats" -> "bat"
def tokenize(text):
  # remove affixes
  stem = nltk.stem.SnowballStemmer('english')
  # set the text to lower case
  text = text.lower()

  for token in nltk.word_tokenize(text):
    # strip punctuation
    if token in string.punctuation: continue
    yield stem.stem(token)

# ------- Frequency Vectorize
# Frequency vectors fimply fill in the vector with the frequency of each word.
# Each doc is represented as the multiset of the tokens
# NLTK expects features a dict object whose keys are the the name of the features, whose values are boolean or numeric
# to todo this we create the vectorization method

# - create a dictionay whose keys are the tokens in the doc (corpus doc) and values are the number of time that token appears
def nltk_frequency_vectorize(doc):
  # defaultdict allows us to specify what the dictionary will return for a key that hasn't been assigned
  from collections import defaultdict
  # specify that 0 should be returned in case
  features = defaultdict(int)
  for token in tokenize(doc):
    # map to every item
    features[token] += 1
  return features

vectors = map(vectorize, corpus)
for value in vectors:
  print(value)

# In Scikit-learn
# - CountVectorizer transformer from the sklearn.feature_extration model has its own tokenization and normalization
# - fit method expets an itterable, list of strings r file objects and creates a dictionary
# - each doc is turned into a sparse array, tupel, row id and value is the count
def sklearn_frequency_vectorize(corpus):
  from sklearn.feature_extraction.text import CountVectorizer
  vectorizer = CountVectorizer()
  return vectorizer.fit_transform(corpus)

# Gensim frequency encoder is called doc2bow. 
# - create Gensim dictionary: maps tokens to the indices base on the observed order
# - dictionary can be loaded or saved to disk
# - it implements doc2bow library that accepts a pretokenized document and returns a sparse matrix of (id, count) tupels
# - doc2bow only takes a single docuemnt instance, we use list comprehension to restor the corpus
# - load the tokenized docuement into memory to not exhaust generator
def gensim_frequency_vecotrize(corpus):
  import gensim
  corpus = [tokenize(doc) for doc in corpus]
  id2word = gensim.corpora.Dictionary(corpus)
  vectors = [
    id2word.doc2bow(doc) for doc in corpus
  ]
  return vectors


# ------- ONE HOT ENCODING
# Tokens that occur very frequently are orders of magnitued more "significant" than other, less frequent
# One-hot encoding is a bollena vector encoding method that marks a particular vector index with a 1 if the token exists
# or 0 (false) if it does not.
# - reduces the imbalance issue of the distribution of tokens.
# - simplifies a document to its constituent components.
# - most effective for small documents (sents, tweets)
# - applied to modes that have very good smooting properties
# - use in NNs

# dictionaries act as sparse matricies in NLTK
# not necessary to make every absent word False
def ntlk_onehot_vectorization(corpus):
  def vectorize(doc):
    return {
      token: True for token in doc
    }
  vectors = map(vectorize, corpus)
  return vectors

# - onehot is implement with Binarizer transformer
# - text data must be transformed to numeric space using CountVectorizer
# - Binarizer uses threshold value (0 default)
# - those that are greater than threshold are set to 1
def scikit_learn_onehot_vectorization(corpus):
  from sklearn.preprocessing import Binarizer
  from sklearn.feature_extraction.text import CountVectorizer

  freq = CountVectorizer()
  corpus = freq.fit_transform(corpus)

  onehot = Binarizer()
  # toarray() convers the sparse matrix representation to a dense one. Corpora with large vocabs better to have
  # a sparse matrix
  corpus = onehot.fit_transform(corpus.toarray())

# ** One-hot encoding represent similarity and difference at the document level, cuz words are equidistant, it is not
# able to encode per-word similarity. Normalizing tokens ensures that different forms of tokens are treate as a single vector,
# reducing featurespace.
# we can one-hot encode our vectors with our id2word dictionary
# conver the list of tuples returned by doc2bow into a list (token_id, 1)
def gensim_onehot_vectorization(corpus):
  import gensim
  corpus = [tokenize(doc) for doc in corpus]
  # - create Gensim dictionary: maps tokens to the indices base on the observed order   
  id2word = gensim.corpora.Dictionary(corpus)
  # - it implements doc2bow library that accepts a pretokenized document and returns a sparse matrix of (id, count) tupels
  # Gensim frequency encoder is called doc2bow. 
  vectors = [
    [(token[0], 1) for token in id2word.doc2bow(doc)]
    for doc in corpus
  ]
  return vectors

# ------- TF-IDF Term Frequency-Inverse Document Frequency
# consider the relative frequency or rareness of tokens in the document against thier frequency in other documents
# meaning is most likely encoded in the more rare terms from a documents
# TF-IDF normalizes the frequency of tokens in document with respect to the rest of the corpus.
# it accentuates terms that are very relevant to the specific instance.
# - computed on a per term basis
# - the more informative that term is to that document the closer to 1.
# - the less the closer to 0


# we use TextCollection for a list of texts or corpus consisting of one or more texts.
# provide support for counting, concordancing, collocation, and computing tf_df
# tf-idf requies the entire corpus
# - accept all documents
# - create a text collection
# - yield a dictionary whose keys are the terms and values are the TF-IDF score
def nltk_tfidf_vectorize(corpus):
  from nltk.text import TextCollection

  def vectorize(corpus):
    corpus = [tokenize(doc) for doc in corpus]
    texts = TextCollection(corpus)
    
    for doc in corpus:
      yield {
        term: texts.tf_idf(term, doc)
        for term in doc
      }

# Driver code to check above generator function
# for value in [tokenize(set) for sent in corpus] : 
#     print(value)
  