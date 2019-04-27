from random import choice

def sampleWords(words):
  '''
  Function takes corpus and generates a random sentence based on it.
  '''
  corpus = str(words).replace('.', ' $Stop $Start')
  corpus = str(corpus).replace('!', ' $Stop $Start')
  corpus = str(corpus).replace('?', ' $Stop $Start')
  corpus = corpus.replace('"', '')
  corpus = corpus.split()
  pairs = make_pairs(corpus)
  dict = {}
  for word1, word2 in pairs:
    if word1 in dict:
      dict[word1].append(word2)
    else:
      dict[word1] = [word2]
  start = choice(dict['$Start'])
  output = [start]
  running = True
  while running:
      item = choice(dict[output[-1]])
      if item == '$Stop':
        running = False
      else:
        output.append(item)
  return ' '.join(output)

def make_pairs(corpus):
  for i in range(len(corpus)-1):
    yield (corpus[i], corpus[i+1])

if __name__ == '__main__':
  book = open('book.txt', 'r').read()
  print(sampleWords(book))