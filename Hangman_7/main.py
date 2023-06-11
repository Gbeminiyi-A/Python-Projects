import click

import random

from hangman_words import word_list


def clrscr():
    # Clear screen using click.clear() function
    click.clear()


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages

print(logo)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clrscr()

    if guess in display:
        print(f'You guessed {guess}, you have entered this before')
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:

        if guess not in chosen_word:
            print(f'you guessed {guess}, that\'s not in the word.')
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
