import HTMLCorpusReader

path = '/Users/esaavedra/Work/personal/projects/applied-text-analysis/ignore/baleen/export'
html = HTMLCorpusReader.HTMLCorpusReader(path)

# books = html.docs(None, 'books')

# print(books)

# for content in books:
#   print(content)

# bookSizes = html.sizes(categories='books')

# for size in bookSizes:
#   print(f"{(size/1024):.2f} KB")
# data = html.sents(None, 'books')
# for item in data:
#   # print(doc.title())
#   # print(doc)
#   print(item)


# data = html.tokenize(None, 'books')
# for paragraph in data:
#   # print(doc.title())
#   # print(doc)
#   for sent in paragraph:
#     for tag, token in sent:
#       print(f"{tag} - {token}")

print(html.describe(None, 'books'))