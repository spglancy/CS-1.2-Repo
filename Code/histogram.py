from pprint import pprint
str = "it a string a string string"
def histogram_dict(str):
  str = str.split()
  count = {}
  for i in str:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
  return count

def histogram_list(str):
  dict = histogram_dict(str)
  output = []
  for i in dict:
    output.append([i, dict[i]])
  return output

def histogram_tuple(str):
  dict = histogram_dict(str)
  return output.items()

def histogram_count(str):
  dict = histogram_dict(str)
  output = {}
  for i in dict:
    if dict[i] in output:
      output[dict[i]].append(i)
    else:
      output[dict[i]] = [i]
  output = output.items()
  return output

def unique_words(hist):
  return len(hist.values())

if __name__ == '__main__':
  val = histogram_list(str)
  # val2 = unique_words(val)
  print(val)
  # print(val2)