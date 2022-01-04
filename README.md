In order to leverage the data encoded in language we need break things up.

## Token
Unit of text analysis. A string of encoded bytes that represent text. "word sense" (noun,verb etc ..., ex: crab-nl)

## words symbols representative of meaning.
Words do not have a fixed universal meaning independet of context such as culture and language.

## Goal
select model family to mininmize error, fitted model can make predictions returning label, probabilities, membership or values. Challange is to strike a balance between being able to precisely learn the patters in the known data and being able to generalize so the model perfoms well on examples it has never seen.

## Tools
- Scikit-Learn
  - API for generalized machine learning.
- NLTK
  - Toolkit with pretrained models
- Gensim
  - unsupervised sematic modeling of text. Originally designed to find similarity between documents. See `word2vec`
- spaCy
  - production grade language processing.
  - preprocessing text for deep learing or to build information extraction
- NetworkX
  - using graphs to manipulate complex nextworks.
  - able to encode complex relationships
- Yellowbrik
  - Used to visualize network workflows.

## Workflow
- Select model. It is composed of features, algorithm and hyperparameters that best operates on trainin data to produce estimations on unknown data.
- We create training dataset called **Corpus** in text anaylsis
- Feature extraction and preprocessing methods, to compose **text as numeric data**
- With basic features we explore techniques for classification and clustering on text.

## Example Repository
[link](https://github.com/foxbook/atap)