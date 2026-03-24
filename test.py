from collections import Counter

word = input("Enter a word: ").lower()
word2 = input("Enter another word: ").lower()

print(Counter(word) == Counter(word2))