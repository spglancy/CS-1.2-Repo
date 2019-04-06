import random
import sys

def rearrange(words):
  for i in range(len(words)-1):
    # picks an index to swap to
    val = random.randint(0, len(words)-i-1)
    words[i], words[val] = words[val], words[i]
  return ' '.join(words)

def flip(text, bool):
  if bool == '1':
    text = text.split()
    text.reverse()
    return ' '.join(text)
  elif bool == '0':
    text = list(text)
    text.reverse()
    return ''.join(text)

def anagram(text):
  text = rearrange(list(text))
  return text.replace(" ", "")

if __name__ == '__main__':
  print(rearrange(sys.argv[1:]))
  # print(flip(sys.argv[1], sys.argv[2]))
  # print(anagram(sys.argv[1:]))