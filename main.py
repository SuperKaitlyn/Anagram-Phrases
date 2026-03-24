import load_dictionary


word_list = load_dictionary.load('2of4brif.txt')
anag_list = []
user_word = input('Enter ANY word here: ')
user_word = user_word.lower()
for word in word_list:
    if sorted(word) == sorted(user_word) and user_word != word:
        anag_list.append(word)
        anag_list.append(word)
print(f"Count of anagrams: {len(anag_list)}\n",*anag_list, sep="\n")

