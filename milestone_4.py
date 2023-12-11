import random

class Hangman:
    secret_word = ""

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.secret_word = random.choice(word_list)
        self.list_of_guesses = []
        self.word_guessed = ['_' for _ in self.secret_word]

    def check_guess(self, guess):
        print(self.secret_word)
        if self.secret_word.__contains__(guess.lower()):
            print("Good guess! " + guess + " is in the word.")
            self.list_of_guesses.append(guess)

            # Update the word_guessed list based on the correct guess
            for i in range(len(self.secret_word)):
                if self.secret_word[i].lower() == guess.lower():
                    self.word_guessed[i] = guess.lower()

            print(self.word_guessed)
        else:
            print("Sorry, " + guess + " is not in the word. Try again.")

    def ask_for_input(self):
        for _ in range(len(self.secret_word)):
            guess = input("Try to guess a letter: ")
            if guess.isalpha():
                self.check_guess(guess)
                print("Remaining guesses: " + str(self.word_guessed.count('_')))
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
                self.check_guess(guess)

test = Hangman(["ciao", "peppe"])