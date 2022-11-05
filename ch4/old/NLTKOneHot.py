# one-hot encoding is a dictionary whose keys are tokens and whose value is TRUE:
def vectorize(doc):
  return {
    token: True
    for token in doc
  }

vectors = map(vectorize, corpus)