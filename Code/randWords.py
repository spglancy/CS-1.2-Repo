import random
import sys

def randomWord(numWords):
  file = open("/usr/share/dict/words", "r")
  words = file.read().split()
  output = []
  for i in range(int(numWords)):
    output.append(words[random.randint(0, len(words)-1)])
  return ' '.join(output)
if __name__ == "__main__":
  print(randomWord(sys.argv[1]))