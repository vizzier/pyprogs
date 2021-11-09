# fancy a game of hanngman?? :-p
import random
import sys


words_to_guess = ['python', 'java', 'kotlin', 'javascript']

print(*'HANGMAN')


# the game itself
def guess(word):
    tries = 8  # number of attempts to guess the word
    letters = []
    index = []
    wrong_letters = []

    # the main loop that searches for user inputed letters in a guessed word
    while tries > 0:
        for letter in letters:
            start = 0
            counter = 0
            while counter < word.count(letter):
                index.append(word.find(letter, start))
                start = word.find(letter, start) + 1
                counter += 1

        # the condition to win (number of guessed letters equal to number of letters in the word)
        if len(set(index)) == len(word):
            print(f'''You guessed the word {word}!
You survived!''')
            break  # breaking out of our tries loop when you guessed the word

        print('')

        # block for printing the word with guessed letters and yet not guessed letters
        for j in range(len(word)):
            if j in index:
                print(word[j], end='')
            else:
                print('-', end='')

        print('')
        user_letter = (input('Input a letter: '))  # here user inputs letter by letter


# block that checks for different typos and errors of user input
        if len(user_letter) != 1:
            print("You should input a single letter")
            continue

        elif user_letter.isascii() == False or user_letter.islower() == False:
            print("Please enter a lowercase English letter")
            continue

        elif user_letter in letters or user_letter in wrong_letters:
            print('You\'ve already guessed this letter')
            continue

        elif user_letter not in word:
            print('That letter doesn\'t appear in the word')
            wrong_letters.append(user_letter)
            tries -= 1
            continue

        elif user_letter in word:
            letters.append(user_letter)

    if tries == 0:  # if you are out of attempts, you lost!
        print('You lost!')
    print('')


choice = ['play', 'exit']  # choice to run the script


# menu of the script (options to play or to exit)
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == choice[0]:
        guess(random.choice(words_to_guess))  # takes a random word from a word list to play the game
    elif menu == choice[1]:
        sys.exit(1)
