response = True
while response:
    guess = input("Try to guess a letter: ")
    if guess.isalpha():
        response = False
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
