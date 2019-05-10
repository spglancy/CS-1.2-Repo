from random import choice

def sampleWords(words, order):
  '''
   Function takes corpus and generates a random sentence based on it
  '''
  corpus = str(words).replace('.', '')
  corpus = str(corpus).replace('!', '')
  corpus = str(corpus).replace('?', '')
  corpus = corpus.replace('"', '')
  corpus = corpus.split()
  groups = make_groups(corpus, order)
  dict = {}
  for group in groups:
    if group[0] in dict:
      dict[group[0]].append(group[1])
    else:
      dict[group[0]] = [group[1:]]
  start = choice(dict[choice(list(dict.keys()))])
  output = [start]
  running = True
  r = 0
  while running:
      items = []
      for o in range(order):
        items.append(reversed(output[o]))
        o += 1
      print(items)      
      item = choice(dict[tuple(items)])
      if r == 10:
        running = False
      else:
        output.append(item)
      r += 1
  return ' '.join(output)

def make_groups(corpus, order):
  output = []
  l1 = []
  l2 = []
  for i in range(len(corpus)-order-1):
    for x in range(order):
      l1.append(corpus[i+x])
    output.append((tuple(l1), corpus[i+order]))
    l1 = []
    l2 = []
  return output

if __name__ == '__main__':
  book = open('book.txt', 'r').read()
  print(sampleWords(book, 2))