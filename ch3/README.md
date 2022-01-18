Corpus neds significant preprocessing and compression. 

We need a multipurpose preprocessing framework, with 5 key stages:
  1. Content Extraction
  2. Paragraph Blocking
  3. Sentence Segmentation
  4. Word Tokenization
  5. Part-of-speech tagging

Each will live in the `HTMLCorpusReader` class

We have methods for
  - filtering `resolve()`
  - accessing `docs()`
  - counting `sizes()`

We are extending from the `NLTKs` `CorpusReader`
 - `raw()` The text with no processing
 - `sents()` Generator for individual sentences in the text.
 - `words()` Tokenize text into individual words.

These methods are important to `fit` models using ML

Some other methods provided by NLTK `CorpusReader`
  - auto tagging
  - auto parsing sentences
  - converting annotated text to data structures lik `Tree Objects`

## Paragraphs

Extracting HTML content
`readability-lxml` library for grappling with web documents. It leaves just the text.
It emplys a regex to remove nave bars, adds, scripts, css and build a new DOM tree

important modules
  `$ pip3 install readability-lxml` 
`Unparseable` and `Document`

Paragpraphs as units of document structure

Then we create a preprocessed corpus to facilitate ML.

To read paragraphs the `PlaintextCorpusReader` implements the `paras()` method. A generator of paragraphs defined as blocks of text delimited with double newlines.

To search through text we will use `BeautifulShoup`

## Sentences (Segmentation)
Sentences can be thought of as units of dicourse

`Segmentation` to parse our text into sentences. `SpaCy's` tool often works better with speech data whilt `NLTKs` work better with written language.

We create a `sents()` method to iterate through each paragraph and use the `sent_tokenize` method employing the `PunktSentenceTokenizer` a pre-trained model that has learned transformation rules. 

`sent_tokenize` does well with standard paragraphs but identifying the boundaries between sentences can be tricky. There are also alternative sentence tokenizers (for tweets)

## Tokenization (Individual Tokens/Words)
Tokens are syntatic units of language that encode semantic information within sequences of characters.

We will use `WordPunctTokenizer` a regex-based tokenizer that splits text on both whitespace and punctuation and returns a list of alphabetic and non-alphabetic chars.

We have to consider a few things:
 - do we want to to remove punctuation from tokens
 - should we make punctuation marks tokens themselves?
 - should we preserve hyphenated words as compound elements or break them apart?
 - should we approach contractions as on token or two? And if 2 should they be split?

We can select different tokenizers depending on the need. There are many tokenizers
  NTLK
    - `TreebankWordTokenizer`
    - `WordPunctTokenize`
    - `PunktWordTokenizer` which is based on the `RegexpTokenizer` which splits strings using the regex `\w+|[^\w\s]+`
    - `word_tokenize` which invokes the `Treebank` tokenizer and uses regex to tokenize text.

### Part-of-Speech Tagging (see HTMLCorpusReader.tokenize())

We tag each token with "part of speech" (verbs, nouns, prepositions, adjectives). How words function within the context of a sentence.

We use the `NLTK` `pos_tag` and uses the `PerceptronTagger()` and the `Penn` `Treebank` tagset. The Treebank consists of 36 parts of speech, structural tags, and indicator of tense

### Indicator of tense
  - NN (singular nouns)
  - NNS (plural nouns)
  - JJ (adjectives)
  - RB (adverbs)
  - VB (verbs)
  - PRP (personal pronouns)

  Nouns - start with `N`
  Verbs - start with `V`
  Adjectives - start with `J`
  Adverbs - start with `R`

  more info here : https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

"Document decomposition" to extract all data and and tokenize

## Corpus Analytics
See `HTMLCorpusReader.describe()`

## Transformation
We dont want to run our preprocessing everytime and its best to add 2 classes a `Preprocessor` class that wraps `HTMLCopusReader` to wrangle raw corpus to store an intermediate transformed corpus artifact. And `PickledCorpusReader` that can stream the transformed documents from disk in standardized fashion for down stream vectorization and analysis.