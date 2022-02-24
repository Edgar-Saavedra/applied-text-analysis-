## Text vectorization
ML expects algos to operate on a numeric feature space. Expecting input as a 2D array
**ROWS** instances
**Columns** features

We need to transform our documents into vecotr representations. This called **FEATURE EXTRACTION** aka **VECTORIZATION**

Representing documents numerically lets us perform analytics, and create *instances* on which ML can operate.

**Instances** are entire documents or **utterances** (quotes, tweets, entire books), but the vectors are entire uniform length
Each property of a the vector representation is a **feature**

For text features represent attributes and properties of the document, included in content and meta data. Such as length, author, source, publication date. 
Features represent a multidimensional feature space on which ML can be applied.

Shift understanding of language from sequence of words to points that occupy a high-dimensional semantic space. Points can be close together or far apart, clustterd or evenly distributed.

**Semantic Space**  mapped where documents with similar meaning are closer together and those that are different are farther apart.

We will use use techniques from NLTK with learning techniques in Scikit-Learn and Gensim. 
We create custom transformers, that can be used inside repeatable and reusable pipelines.

### Semantic Spaces (Models)

### Bag-Of-Words Model
Primary insight is that meaning and similarity are encoded in vocabularity (aka the similarity has to do with the definitions of words).

1. We represent every document from the corpus as a vector whose length is equal to the vocabulary of the corpus.
2. We simplify computation by sortin token position of the vector into alphabetical order.
3. Or keep a dictioany that maps to tokens to vector position
4. Many of our semantic spaces will extend from bag of words.

We have four types of vector encoding:
 1. Frequency
 2. One-hot
 3. TF-IDF
 4. distributed representations

For testing, create a list of documents and tokenize them
strip punctuation using string.punctuation and setting text to lower case
we also want to reduce features to remove affixes and plurality

The choice of vectorization is driven by the problem space.

## Identifying problem space
**NLTK** offers many methods that are especially suited to te text data, but is a big depency
**Scikit-Learn** was not designed with text in mind, but offers robust API and many conviniences
**Gensim** can serialize dictionaries and references in "matrix market format" making it more flexible for multiple platforms. It doesnt do any work on behalf of your documents for tokenization or stemming.


### Frequency Vectors
- To simply fill in the vector with the **frequency of each word** as it appears in the document.
  - Each document is represented as the **multiset of the tokens** that compose it.
  - Also represented as the value for each word position in the vector is its count.

We can either normalizeencoding where there can be a straight count  or where each word is weighted by the total number of words.

#### Frequency Vectors (NLTK)
NLTK expects features as a `dict` object whose keys are the names of the features and whose values are `boolean` or `numeric`.
- We create a `vectorize` function : creates a dictionary whose keys are the tokens in the values are times that token appears in the document.

`defaultdict` object allows us to specify what the dictionary will return for a key that hasn't been assigned to it yet. `defaultdict(int)` creates a simple counting dictionary. It is mapped `map`  to every item. 

See FrequencyVectorNltk.py

#### Frequency Vectors (Scikit-Learn)
The `CountVectorizer` transformer from the `sklearn.feature_extraction` model has its own inter tokenization and normalization methods.
The `fit` method expext an iterable or list of strings or file objects and creates a dictionary of the vocab.
`transform` is called on each document and transformed into a sparse array with an `index` `tuple` with the document id and token ID from the dictionary, the value is the count.

See `FrequencyVectorScikitLearn.py`

#### Frequency Vectors (Gensim)
The frequency vector encoder is called `doc2Bow`. 
- Creates a Gensim Dictionary
  - Maps tokens to indices based on "observed" order
- returns sparse matrix of tupels (id, count)

See `FrequencyVectorGensim.py`

## One-Hot Encoding
Tokes that occur very frequently are order of magnitude more "significant" than other, less frequent ones which can impact noramlly distributed features. One-hot encoding is a boolean vector encoding method that marks a particular vect index with a value of 1 (true) if the token exists in the document and 0 (false) if it does not.

I t reduces the imbalance issue of the distrubution, simplifying a docuemnt to its constituent components. commonly used in NNs.

## Distrubuted Representation
One-hot, TF-IDF enable us to put documents into vector space. Useful to also encode similarities between documents in the context of that same vector space. We encode docuemtns along a continuous sclae with a distributed representation. 

**The Complexity** of this space is the product of how the mapping to that representation is learned. The product of how that representation is trained, not directly tied to the document itself.

### word2vec
Algorithm trains word representations based on the either a continous bag-of-words or skip diagram model.
Words are embedded in space along similar words based on their context.

### doc2vec
extension of word2ved. Proposes **paragraph vector** an **unsupervised algo**. Attempts to inherit the semantic properties of words. Takes into consideration the ordering of words within a narrow context.

Vectorization Method | Function | Good For | Considerations

Frequency - Counts term frequencies - good for Bayesian Models - Most frequent words sometimes not most informative
One-Hot Encoding - Binarizes term occurrence - NNs - All word equidistant, so normalization very important
TF-IDF - Normalizes term frequencies accross documents - General Purpose - Moderaltly frequent terms may not be representative of docuemtn topics
Distributed Representations - Context-based, continuous, term similarity encoding - modeling more complex relationships - performance intensive; difficult to scale without tools (tensorflow)