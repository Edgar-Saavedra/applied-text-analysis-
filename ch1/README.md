Data science a mix of professions. Statistician, computer scientis, domain expert. Data scientists bridge work done in an academic context. Data science workflow not always compatible with Software Development practices.

Data Science Team -> Managment -> Tech Lead -> Dev Team -> product

Important to know how to build a large corpus, how to transform raw documents into usable data.

## Language Aware Data Products
Drive their value from data and generate new data in return.
No only reponsive to human input can adapt to change.

Example: Yelp insights. Uses sentiment analysis and significant collocation (words that tend to appear together). It uses a **domain specific corpus**. Automatic indentification of significant sentences.

Example: "suggested tag" tags indentify properties of the content they describe.

## Data product pipeline
Itterative process consistin of 2 phases : build and deploy.
- Build phase: data is ingested and wrangled into a form that allows models to be fit and experiment on.
- Deploy phase: models are selected and then used to make estimations or predictions.
- Interaction
  - Feedbac -> Ingestion
- Data
  - Wrangling
  - API
- Storage
  - Normalization
  - Model selection & Monitoring
- Computation
  - Feature analysis/model builds
  - Cros validation.
TL;DR: 
Build phase ingests data, wrangles it to a form that allows model to be fit and experiment.
Deploy phase - takes selected models and uses it to make estimates and predictsions.


### Models 
Relationship of variables to the target. An instance of features, algorithm and hyperparameters.
Fitted models ia s model form that has been fit to a specific set of training data and can make predictions.

We need to change how we see language and see it a numberic data.

### Language as data
Language is *unstructured* and governed by lingustic properties.
**Structured or Semistructured** data includes fiels or markup that enable it to be easily parsed by a computer.

Supervised learning is usually implement in text analysis.

**corpora** our training data

We assume text is predicatable.

- Take **tokens** strings of data, give a context and define a **constrained numeric decision space** on which models can compute.

**types of natural language processing**
- Phologic
- syntatic
- semantic

## STEPS
1. Identify features of data. 
2. Context modifies, interpretation
3. Create a the traditional **bag-of-words** model

### nltk
- methods
  - `sent_tokenize` Tokenize a sentence from a paragrahp
  - `word_tokenize` gather all words in a tokenized sentence and tokenize them

## Sentiment Analysis
Very popular text classification technique to get the tone of text and can lead to aggregate analysis. Is fundamentally different from gender classification that is dependent on **word sense**, **contenxt**. It can be negated. Many models take into account localization of words in their context.

## Bag-of-words
Simple modle that evaluates the frequency with which words appear and appear with others in a specif limted context (co-occurences). Co-occurences show which words are likely to proceed and succeed each other. Whic allow us to make inferences on limited pices of text.

## Word ordering
We can use statistical inference methods to make predictions about word ordering. We can find correlation of words and phrases. This part of **n-gram analysis** n specifies a ordered sequence of either characters or words to scan. It requires some ability to learn the relationship of text to some targe variable.

Laguage features and contextual ones contribute to the overall predictabiility of language for analytical puposes.

## Structural features
Important to consider high-level units of language used by linguistics, which give us a vocabulary for the operation we'll perform

Different units of language are used to compute at a variety of levels.

**semantics** refer to meaning, deeply encoded in language, difficulte to extract. There is a template (subject, predicate, object)

**ontologies** can be made from the templates and define the relationships between entities.Requires knowledge of teh context and the domain, does not scale well.

**Semantic analysis** is about understanding meaning of text but about generating data structures to which logical reasoning can be applied.
"Themantic meaning representations" (TMRs) to which first-order logic of "lambda" calculus can be applied 
Networks can be used to encode predicate interactions of features.
Traversal can be used to analyze the centrality of terms or subjects.
Graph analysis can produce insights.

**Syntax**
Formation rules defined by grammar. Syntatic analysis used to show relationship of words. Relationship of tokes in a tree structure. How words modify each other in the formation of phrases.

**morphology** The form of things. The form fo individual words or tokens. Plurality, tense, conjugation. Tough due to special cases. To understand the parts of wors so we can assign them to classes. **PART OF SPEECH** tags. To know if singular noun, plural noun, proper noun, verb is conjugated.

Vectorization is applid to these structures to create numeric feature spaces.