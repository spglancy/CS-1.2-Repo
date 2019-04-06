from pprint import pprint
def get_words(filename):
  '''Open the file and return all words in it'''
  words_list = []
  with open(filename) as file:
    for line in file:
      words = line.split()
      for word in words:
        words_list.append(word)
    return words_list

def count_animals(animals_list):
  '''count the amount of times each animal appears'''
  animal_counts = {}
  for animal_name in animals_list:
    if animal_name in animal_counts:
      animal_counts[animal_name] += 1
    else:
      animal_counts[animal_name] = 1
  return animal_counts

def print_table(animal_counts):
  '''print out a table of animals and their counts'''
  print('Animal | Count')
  print('--------------')
  for animal in animal_counts:
    print('{} | {}'.format(animal, animal_counts[animal]))

print_table(count_animals(get_words('animals.txt')))