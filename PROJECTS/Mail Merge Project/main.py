PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as namesfile:
    names = namesfile.readlines()

with open('./Input/Letters/starting_letter.txt') as letter:
    letter_content = letter.read()
    for name in names:
        name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, name)
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as f_letter:
            f_letter.write(new_letter)
    
