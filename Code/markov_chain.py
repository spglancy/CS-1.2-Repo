from random import choice
import dictogram
import sampling

def sampleWords(words, order):
  '''
   Function takes corpus and generates a random sentence based on it
  '''
  corpus = str(words).replace('.', ' $Stop $Start')
  corpus = corpus.replace('!', ' $Stop $Start')
  corpus = corpus.replace('?', ' $Stop $Start')
  corpus = corpus.replace(',', '')
  corpus = corpus.replace('(', '')
  corpus = corpus.replace(')', '')
  corpus = corpus.replace(';', '')
  corpus = corpus.replace(':', '')
  corpus = corpus.replace('"', '')
  corpus = corpus.replace("'", '')
  corpus = corpus.split()
  groups = make_groups(corpus, order)
  dict = {}
  for group in groups:
    if group[0] in dict:
      dict[group[0]].add_count(group[1])
    else:
      dict[group[0]] = dictogram.Dictogram([group[1]])
  output = []  
  current = ('$Stop', '$Start')
  running = True
  while running:
    word = sampling.sample(dict[current])
    current = list(current[1:])
    current.append(word)
    current = tuple(current)
    if word == '$Stop':
      running = False
    else:
      output.append(word)
  return ' '.join(output)

def make_groups(corpus, order):
  output = []
  key = []
  for i in range(len(corpus)-order):
    for x in range(order):
      key.append(corpus[i+x])
    output.append((tuple(key), corpus[i+order]))
    key = []
  return output

if __name__ == '__main__':
  book = open('book.txt', 'r').read()
  print(sampleWords(book, 2))