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

Sorts copora in to categories and subcategories.

Stores files as HTML files, named according to ther **MD5** hash (prevent duplication)
**citation.bib**, **LICENSE.md** and **README.md** are special files automatically read from and NLTK CorpusReader object with the
`citation()` `license()` and `readme()` methods.

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

For smaller applications a file based approach might be better.

## Corpus Disk Structure

Simplest approach is to store individual documents in a file system. Corpora stored on disk are generallly static and treated as a whole. Smaller files do not make sense to store in individual files. Things like email are stored in **MBox format**. Tweets are generally stored as **JSON**. A copus represents many files.

**MBox format** a plain text format that uses seperators to delimit multipart mime messages containing txt, THML, images, and attachemnts

**NLTK CorpusReader** objects can read from either a path to a director or ZIP.

## Corpus Reader
After organized on disk, we can access the corpus in a programming context, and monitor change. Text strings are loaded from the documents. It is a programmatic interface to read, seek, stream and filter documents a expose data wrangling techniques. You often need a application specific corpus reader.

Streaming accesses of a corpus from disk are all thought by the NLTK library which exposes corpora in Python via `CorpusReader`

**Hadoop** distributed computing framework. We will use Spark a successor of Hadoop.

## Streaming Data Access with NLTK

NLTK comes with generic utility Corpus Reader Objects

### PlaintextCorpusReader
Consists of plain-text documents, where paragraphs are assumed to be split using blank lines.

### TaggedCorpusReader (annotated, for domain-specific hand annotation)
Where sentences are on their own line and tokens are delimted with their tag.

### BracketParseCorpusReader (annotated, for domain-specific hand annotation)
Parenthesis-delineated parse trees.

### ChunkedCorpusReader (annotated, for domain-specific hand annotation)
Corpus of tweets, delimtted JSON

### WordListCorpusReader
List of words on per line.

### XMLCorpusReader
XML files

### CategorizedCorpusReader
Organized by category.

### CategorizedPlaintextCorpusReader
For accessing movie scripts. Weneed to specify a regular expression that allow the reader to automatically determin both the fileids and categories. That ther is one or more letters digits, spaces or underscores followed by /

```
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

DOC_PATTERN = r'(?!\.)[\w_\s]+/[\w\s\d-]+\.txt'
CAT_PATTERN = r'([\w_\s]+)/.*'

corpus = CategorizedPlaintextCorpusReader(
  'path/to/corpus/root', DOC_PATTERN, cat_pattern=CAT_PATTERN
)
```

### HTML Corpus
We can create a streaming corpus reader top stip all tags from HTML write is a plain text and using the `CategorizedPlaintextCorpusReader` but we will lose benifits of HTML. Allows user to specify which HTML tags should be treated as independent paraphs we create and Augment the HTMLCorpusReader with a method that will allow us to filter how we read text data from disk. The reader exposes the entire text of every single document in the corpus in a stream fashion t our methods.
