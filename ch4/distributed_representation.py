# Often important to encode the similarities between documents in vector space
# also encode the similarities between documents.
# we wont be able to compare documents that don't share terms

# We encode text along a continuous scale with a distributed representation.
# a document is prepresented in a feature space that has been embedded to represent similarity.
# The "complexity" of this space is the product of thw the mapping to that representation is learned.
# The "complexity" of this space is the product of how that representation is trained and not direclty tied to the document

# Word2vec: trains word representations based on either a continuous BOW or skip gram model. Words are embedded in space alongwith similar words based on their context.
# doc2vec: unsupervised algo, attemps to inherit the semantic properties of words such that "red" and "colorful" are more
# similar to each other than they are to "river" or "governance".
# Takes into consideration the order of words within a narrow context.
# it generalizes better and has a lower dimensionality

# ----- GENSIM
# 1. use a list comprehension to load our corpus
# 2. Create a list of TaggedDocument objects wich extend LabeledSentence and in turn the distributed representation of word2vec
# 3. TaggedDocument objects consist of words and tags.
# 4. once we have a list of tagged documents we instanciate the Doc2Vec model and specify the size of the vectors and minimum count
# the size parameter is usually not as low as dimensionality 4.

# Distributed Representation will imporve results over TF-IDF models when used correctly.
# The model can be saved to disk
# retrained, in a active fashion
# Slow on large corpora
# might not be as good as Principal Component Analysis (PCA) or Singular Value Decomposition (SVD) applied to reduce feature space.

from vectorization import tokenize
from vectorization import corpus


def gensim_distributed_representation(corpus):
  from gensim.models.doc2vec import TaggedDocument, Doc2Vec

  corpus = [list(tokenize(doc)) for doc in corpus]
  corpus = [
    TaggedDocument(words, ['d{}'.format(idx)]) for idx, words in enumerate(corpus)
  ]

  model = Doc2Vec(corpus, vector_size=5, min_count=0)
  print(model.dv[0])
  return model

gensim_distributed_representation(corpus)