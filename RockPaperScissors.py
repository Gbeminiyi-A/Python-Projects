rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random  # imported the random module

# Asked the user for their input to know which option they selected
choice = int(input('What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors. '))

# using a try and except function to catch errors such as selecting numbers not in the option
try:
    # created a list with the options for the user
    users_list = ['rock', 'paper', 'scissors']

    # created a variable to store the choice of the user
    user_choice = users_list[choice]

    # used an if statement to print what the user selected and the ASCII
    if choice == 0:
        print(f'You chose {user_choice}')
        print(rock)
    elif choice == 1:
        print(f'You chose {user_choice}')
        print(paper)
    elif choice == 2:
        print(f'You chose {user_choice}')
        print(scissors)

    # created a random function for the computer to select their option
    computers_choice = random.randint(0, 2)

    # created a list too for the computer   'Note to self, I should have probably used the same list from the user
    computers_list = ['rock', 'paper', 'scissors']

    # created a variable to store in the computer's choice and then printed it out along with its ASCII
    computers_choices = computers_list[computers_choice]

    print(f'Computer chose {computers_choices}')

    choices = [rock, paper, scissors]

    print(choices[computers_choice])

    # then finally, I used all the possible combinations to create a Rock Paper Scissors game
    if user_choice == 'paper' and computers_choices == 'paper':
        print('Draw!')

    elif user_choice == 'scissors' and computers_choices == 'scissors':
        print('Draw!')

    elif user_choice == 'rock' and computers_choices == 'rock':
        print('Draw!')

    elif user_choice == 'rock' and computers_choices == 'paper':
        print('You Lose!')

    elif user_choice == 'paper' and computers_choices == 'rock':
        print('You win!')

    elif user_choice == 'rock' and computers_choices == 'scissors':
        print('You win!')

    elif user_choice == 'scissors' and computers_choices == 'rock':
        print('You lose!')

    elif user_choice == 'paper' and computers_choices == 'scissors':
        print('You lose!')

    elif user_choice == 'scissors' and computers_choices == 'paper':
        print('You win!')

    else:
        print('You lose!')
except IndexError:
    print('Choose a valid number!!! You would have lost anyways. ')
