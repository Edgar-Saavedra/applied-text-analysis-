from nltk.corpus.reader.api import CorpusReader
from nltk.corpus.reader.api import CategorizedCorpusReader
import os
import codecs

CAT_PATTERN = r'([a-z_\s]+)/.*'
DOC_PATTERN = r'(?!\.)[a-z_\s]+/[a-f0-9]+\.json'
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