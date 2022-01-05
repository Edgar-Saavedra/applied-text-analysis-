## Building a Corpus

Important to figure out which features, properties or dimensions about our text best encode its meaning and underlying structure.

Identification of unique vocabulary words, sets of synonyms, interrelationships between entities and semantic context.

Text analysis as the act of beraking up larger bodies of work into their components: 
  - vocabulary words
  - common phrases
  - syntatctical patterns
We can use statistical mechanism to produce models of language that allow us to augment apps with predictive capabilities.

## Corpus
Collections of realted documents that contain natural language.

It can be broken down to categories of documents which can vary in size (tweets, books), they contain text and metadata and a set of related ideas.

Documents can be broken down to paragraphs (**units of discourse**). 
Paragraphs can be broken down to sentences (**units of syntax**). 
Sentences are made up of words and punctuation (**lexical units**) that indicate general meaning. 
Words are made up of symbols, phonemes affixes, and characters

### Domain specific corpora
Different domains use different language. A model within a domiain can be analyzed better. Fitting modesl in a narrower context the prediction space is smaller.

We start by collecting a single static set of documents and then apply **routine analyses**

## Baleen Ingestion Engine

[Balee](https://baleen-ingest.readthedocs.io/en/latest/about/) (an automated service for blogs to construct a corpus). 

Given an OPML file of RSS feeds, it downloads all the posts from those feeds saves them to MongoDB storage then exports a text corpus.

It collects RSS feeds from 12 categories:
  sports, gaming, politics, cooking and news

methods:
 - `export`

 ## Corpus Data Management
 **Storing** corpora on disk or document database is often preferred.

 We make some assumptions:
 1. The corpora is non-trivial in size.
 2. The language data will come from a source that will need to be cleaned and processed into data structures.

 Data products are often write-once, read-many (WORM).  We need to keep data in a WORM store and prepocessed data can be reanalyzed without reingestion.

 We need to store our data in 2 places (the raw corpus and the preprocessed corpus). Compuntational access to a text corpus will be a complete read of every single document. We can't do in-place updates nor search or select individual documents.

 The best choice is to store data in a NoSQL document storage database:
  allows streaming reads of the documents with minimal overhead