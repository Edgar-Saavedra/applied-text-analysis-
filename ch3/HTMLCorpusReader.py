from tracemalloc import start
from turtle import pos
from nltk.corpus.reader.api import CorpusReader
from nltk.corpus.reader.api import CategorizedCorpusReader
import os
import codecs
from readability.readability import Unparseable
from readability.readability import Document as Paper
import bs4
from nltk import pos_tag, sent_tokenize, wordpunct_tokenize
import time
from nltk import FreqDist

CAT_PATTERN = r'([a-z_\s]+)/.*'
DOC_PATTERN = r'(?!\.)[a-z_\s]+/[a-f0-9]+\.html'
TAGS = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p', 'li']

class HTMLCorpusReader(CategorizedCorpusReader, CorpusReader):
  """
    A corpus reader for raw HTML documents to enable preprocessing
  """

  def __init__(self, root, fileids=DOC_PATTERN, encoding='utf8',
                 tags=TAGS, **kwargs):
        """
        Initialize the corpus reader.  Categorization arguments
        (``cat_pattern``, ``cat_map``, and ``cat_file``) are passed to
        the ``CategorizedCorpusReader`` constructor.  The remaining
        arguments are passed to the ``CorpusReader`` constructor.
        """

        # Add the default category pattern if not passed into the class.
        if not any(key.startswith('cat_') for key in kwargs.keys()):
            kwargs['cat_pattern'] = CAT_PATTERN
        
        CategorizedCorpusReader.__init__(self, kwargs)
        # takes in generic keyword arguments and the CorpusReader will be initialied with the root directory for the copus.
        CorpusReader.__init__(self, root, fileids, encoding)

        self.tags = tags

  def resolve(self, fileids, categories):
    """
    Returns a list of fileids or categories depending on what is passed
    to each internal corpus reader function. Implemented similarly to 
    the NLTK ``CategorizedPlaintextCorpusReader``
    """
    if fileids is not None and categories is not None:
      raise ValueError("Specify fileids or categories, not both")

    # it will use CorpusReader method to compute the fileids associated witht the specific categories
    if categories is not None:
      return self.fileids(categories)
    
    return fileids
  
  def docs(self, fileids=None, categories=None):
    """
    Returns the complete text of an HTML document, closing the document
    after we are done reading it and yielding it in a memory safe fashion.
    """

    # Resolve the fileids and the categories
    fileids = self.resolve(fileids, categories)

    # create a generator, loading one document into memory at a time.
    for path, encoding in self.abspaths(fileids, include_encoding=True):
      with codecs.open(path, 'r', encoding=encoding) as f:
        yield f.read()
  
  # monitoring system for ingestion and preprocessing
  def sizes(self, fileids=None, categories=None):
    """
    Returns a list of tuples, the fileid and size on disk of the file.
    This function is used to detect oddly large files in the corpus.
    """
    # Resolve the fileids and the categories
    fileids = self.resolve(fileids, categories)

    # Create a generator, getting every path and computig filesize
    for path in self.abspaths(fileids):
      yield os.path.getsize(path)

  def html(self, fileids=None, categories=None):
    """
    Returns the HTML content of each document, cleaning it using
    the readability-lxml library
    see https://github.com/buriy/python-readability
    """
    for doc in self.docs(fileids, categories):
      try:
        yield Paper(doc).summary()
      except Unparseable as e:
        print("Could not parse HTML: {}".format(e))
        continue

  def paras(self, fileids=None, categories=None):
    """
    Uses BeautifulSoup to parse the paragraphs from the HTML.
    """
    for html in self.html(fileids, categories):
      soup = bs4.BeautifulSoup(html, 'lxml')
      for element in soup.find_all(TAGS):
        yield element.text
      soup.decompose()
  
  def sents(self, fileids=None, categories=None):
    """
    Uses teh built in sentence tokenizer to extract sentences from the paraphs.
    Note that this method uses BeautifulSoup to parse HTML
    """
    for paragraph in self.paras(fileids, categories):
      for sentence in sent_tokenize(paragraph):
        yield sentence
  
  def words(self, fileids=None, categories=None):
    """
    Uses the built-in word tokenizer to extract tokens from setences.
    Note that this method uses BeautifulSoup to parse HTML content.
    """
    for sentence in self.sents(fileids, categories):
      for token in wordpunct_tokenize(sentence):
        yield 
  
  def tokenize(self, fileids=None, categories=None):
    """
    Segments, tokenizes and tags a document in the corpus.
    """
    # the tagged tokens are represented as (tag, token) tupels
    # the tag is case-sensitive string that specifies how the token is functioning in context
    for paragraph in self.paras(fileids=fileids, categories=categories):
      yield [
        pos_tag(wordpunct_tokenize(sent)) for sent in sent_tokenize(paragraph)
      ]
  
  # start the clock and initialize 2 frequency distributions:
  # 1. coutns - to hold counts of the document substructures
  # 2. tokens - to contain the vocab
  # we'll keep a cout of each paragraph, sentence and word.
  # we then compute number of files and cats and return a dictionary with a statistical summary of our corpus.
  #  - total number: files, categories, paragraph, sentences, words, unique terms, lexical diversity, average umber of paragraphs, average number of sents total processing time
  def describe(self, fileids=None, categories=None):
    """
    Performs a single pass of the corpus and
    returns a dictionary with a variety of metrics
    concerning the state of the corpus.
    """

    started = time.time()

    # structure to perfrom counting.
    counts = FreqDist()
    tokens = FreqDist()

    # data = html.tokenize(None, 'books')
    for paragraph in self.tokenize(fileids, categories):
      counts['paras'] += 1
      for sent in paragraph:
        counts['sents'] += 1
        for word, tag in sent:
          counts['words'] += 1
          tokens[word] += 1
    

    # compute the number of files and categories in the corpus
    n_fileids = len(self.resolve(fileids, categories) or self.fileids())
    n_topics = len(self.categories(self.resolve(fileids, categories)))

    # return data structure with information

    return {
      'files': n_fileids,
      'topics': n_topics,
      'paras' : counts['paras'],
      'sents' : counts['sents'],
      'words' : counts['words'],
      'vocab' : len(tokens),
      # ML models will expec certain features of data lik lexical diversity and number of paragraphs per doc to remain consitent
      'lexdiv': float(counts['words']) / float(len(tokens)),
      'ppdoc' : float(counts['paras']) / float(n_fileids),
      'sppar' : float(counts['sents']) / float(counts['paras']),
      'secs'  : time.time() - started
    }