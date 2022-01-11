import HTMLCorpusReader

path = '/Users/esaavedra/Work/personal/projects/applied-text-analysis/ignore/baleen/export'
html = HTMLCorpusReader.HTMLCorpusReader(path)

books = html.docs(None, 'books')

# print(books)

# for content in books:
#   print(content)

bookSizes = html.sizes(categories='books')

for size in bookSizes:
  print(f"{(size/1024):.2f} KB")