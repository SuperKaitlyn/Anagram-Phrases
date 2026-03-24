#Load a dictionary file and create word list
#2 Accept a name from the user
#Set a limit equal to the length of the name
#Make a string for anagram phrase
# While the length of the phrase(anagram phrase) is less than the limit we set in step 3;
#1. Generate your word list that fit the name given
#2. Show remaining letters to user
#3. Show
import load_dictionary
from collections import Counter

dictionary = load_dictionary.load('2of4brif.txt')
dictionary.append('a')
dictionary.append('i')
dictionary = sorted(dictionary)
#Allows one letter words like 'a' and 'I' to be used in the name

user_name = input('Enter your name: ')
#Collecting the users name

def find_anagrams(name, word_list):
    """read name and dictionary file & display all anagrams in name"""
    nln = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        wlm = Counter(word).lower
        for letter in word:
            if wlm[letter] < nln[letter]:
                test += letter
            if Counter(test) == wlm:
                anagrams.append(word)
        print(*anagrams, sep='\n')
        print()
        print(f"Remaining letters = {name}")
        print(f"Number of remaining letters = {len(name)}")
        print(f"Number of remaining real word anagrams = {len(anagrams)}")

def process_choice(name):

    while True:
        choice = input("Make a choice else Enter to start over or # to end: ")
        if choice == "":
            main()
        elif choice == "#":
            exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter not in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Sorry, this won't work. Make another choice.")
    name = ''.join(left_over_list)
    return choice, name


def main():

    # Use the name variable and strip out any spaces and/or hyphens

    name = ''.join(user_name.lower().split())
    name = name.replace('-', ' ')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', ' ')
        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase = {len(temp_phrase)}")

            find_anagrams(name, dictionary)
            print(current)


