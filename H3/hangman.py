#! /usr/bin/env python

from words import word_list
import random


def select_word():
    word = random.choice(word_list)
    return word.upper()


def hangman(tries):
    stage = [ """
                  _
                  |
                  |
                  |
                  |
                  |
                 _|_
                / | \\
              """,
              """
                  ________
                  |
                  |
                  |
                  |
                  |
                 _|_
                / | \\
              """,
              """
                  ________
                  |      |
                  |
                  |
                  |
                  |
                 _|_
                / | \\
              """,
              """
                  ________
                  |      |
                  |      O
                  |
                  |
                  |
                 _|_
                / | \\
              """,
              """
                  ________
                  |      |
                  |      O
                  |      |
                  |      |
                  |
                 _|_
                / | \\
              """,
              """
                  ________
                  |      |
                  |      O
                  |     /|
                  |      |
                  |
                 _|_
                / | \\
              """,
              """
                  ________
                  |      |
                  |      O
                  |     /|\\
                  |      |
                  |
                 _|_
                / | \\
              """,
              """
                  ________
                  |      |
                  |      O
                  |     /|\\
                  |      |
                  |     /
                 _|_
                / | \\
              """,
              """
                  ________
                  |      |
                  |      O
                  |     /|\\
                  |      |
                  |     / \\
                 _|_
                / | \\
              """
            ]
    return stage[tries]


def game(word):
    complete = '_' * len(word)
    correct = False
    letters = []
    words = []
    tries = 0

    print(hangman(tries))
    print(complete)
    print('\n')

    while not correct and tries < 8:
        guess = input("Guess a letter or the whole word: ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in letters:
                print("This letter has already been guessed!")
            elif guess not in word:
                print("Wrong guess!")
                tries += 1
                letters.append((guess))
            else:
                print("Correct guess!")
                letters.append(guess)
                letter_list = list(complete)
                pos = [i for i, letter in enumerate(word) if guess == letter]
                for ind in pos:
                    letter_list[ind] = guess
                complete = "".join(letter_list)
                if '_' not in complete:
                    correct = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words:
                print("This word has already been guessed!")
            elif guess != word:
                print("Wrong guess!")
                tries += 1
                words.append(guess)
            else:
                correct = True
                complete = word
        else:
            print("Invalid guess!")

        print(hangman(tries))
        print(complete)
        print('\n')

    if correct:
        print("The word has been guessed!")
    else:
        print("No more tries left!")
        print("The word was " + word)



def main():
    while True:
        word = select_word()
        game(word)
        ans = input("Do you want to play again?[y/n]: ")
        if ans == 'n':
            break


if __name__ == "__main__":
    main()
