import random
import sys

def rearrange(words):
  for i in words:
    val1 = random.randint(0, len(words)-1)
    val2 = random.randint(0, len(words)-1)
    words[val1], words[val2] = words[val2], words[val1]
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
  print(anagram(sys.argv[1]))