import random

words_list = ['banana', 'apple', 'grape', 'peach', 'kiwi']
word = random.choice(words_list)

def check_guess(word):
    words_list = ['banana', 'apple', 'grape', 'peach', 'kiwi']
    secret_word = random.choice(words_list)
    if secret_word.__contains__(word.lower()):
        print("Good guess! " + secret_word + " is in the word.")
    else:
        print("Sorry," + secret_word + " is not in the word. Try again.")

def ask_for_input():
    response = True
    while response:
        guess = input("Try to guess a letter: ")
        if guess.isalpha():
            response = False
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        check_guess(guess)
ask_for_input()
