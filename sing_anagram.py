import load_dictionary
from collections import Counter

dictionary = load_dictionary.load('2of4brif.txt')
word_list = dictionary.lower

user_name = input("Hand over your name: ")
name_count = Counter(user_name)
print(name_count)

for word in word_list:
    if name_count == Counter(word):



print(load_dictionary.load('2of4brif.txt'))

"""user_name = input("Hand over your name: ")
word = 'forest'
name_count = Counter(name)
print(name_count)
word_count = Counter(word)
print(word_count)

if word_count == name_count:"""""


