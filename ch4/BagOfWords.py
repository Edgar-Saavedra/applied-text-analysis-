import nltk
import string

# may examples will use this tokenize method.
def tokenize(text):
  """
    Performes some lightweight normalization, stripping punctuation using string.punctuation and setting text to lowercase.
    Feature reduction is done with SnowballStemmer to remove affixes such as plurality "bats" and "bat" are the same token.
  """
  stem = nltk.stem.SnowballStemmer('english')
  text = text.lower()

  for token in nltk.word_tokenize(text):
    if token in string.punctuation: continue
    yield stem.stem(token)

corpus = [
  "The elephant sneezed at the sight of potatoes.",
  "Bats can see via echolocation. See the bat sight sneeze!",
  "Wondering, she opened the door to the studio."
]
