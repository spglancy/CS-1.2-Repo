import random
import sys

def rearrange(words):
  for i in words:
    val1 = random.randint(0, len(words)-1)
    val2 = random.randint(0, len(words)-1)
    words[val1], words[val2] = words[val2], words[val1]
  return ' '.join(words)
if __name__ == '__main__':
  print(rearrange(sys.argv[1:]))