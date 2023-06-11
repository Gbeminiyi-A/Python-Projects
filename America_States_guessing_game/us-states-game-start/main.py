import turtle
import pandas
from name import Name

name = Name()
screen = turtle.Screen()
screen.setup(750, 600)
screen.title('U.S. States Game')
image = "C:/Users/OLUWAGBEMINIYI/Documents/100 days of code/DAY 25/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv('C:/Users/OLUWAGBEMINIYI/Documents/100 days of code/DAY 25/us-states-game-start/50_states.csv')
correct_states = []
answer = screen.textinput('Guess the state', 'Guess a state').title()

while True:

    state = data[data['state'] == answer]
    countries = data['state'].tolist()
    if answer == 'Exit':
        states_to_learn = [i for i in countries if i not in correct_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv('states_to_learn.csv')
        break

    if answer in countries:
        correct_states.append(answer)
        name.location(state['x'].item(), state['y'].item(), answer.upper())

    answer = screen.textinput(f'{len(correct_states)}/50 States Correct', 'Guess another state').title()
