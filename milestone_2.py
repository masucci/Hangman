import random

words_list = ['banana', 'apple', 'grape', 'peach', 'kiwi']
word = random.choice(words_list)
print(word)

print("Insert a letter:")
guess = input()

if len(guess) == 1:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")
