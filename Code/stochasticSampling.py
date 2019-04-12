from histogram import histogram_dict
from random import randint
def sample(input):
  dict = histogram_dict(input)
  num = randint(0, sum(dict.values()))
  for i in dict:
    num -= dict[i]
    if num <= 0:
      return i

def multisample(input, tests):
  output = {}
  while tests > 0:
    val = sample(input)
    if val in output:
      output[val] += 1
    else:
      output[val] = 1
    tests -= 1
  return output

if __name__ == '__main__':
  print(multisample("this is words so many words are a thing and its rains diamonds on neptune woah woah thats crazy oh my god", 50))