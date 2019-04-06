import random
import sys

file = open("/usr/share/dict/words", "r")
words = file.read().split()

def randomWord(numWords):
  output = []
  for i in range(int(numWords)):
    output.append(words[random.randint(0, len(words)-1)])
  return ' '.join(output)
if __name__ == "__main__":
  print(randomWord(sys.argv[1]))