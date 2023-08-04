#Exercise of Questions and Answers using NBA events.

import os

questions_base = [
    {
        'Question': 'Which Team won the last NBA Finals?',
        'Options': ['Miami', 'Denver','Celtics', 'Brooklyn'],
        'Answer': 'Denver',
    },
    {
        'Question': 'Who was the MVP in the the last NBA season?',
        'Options': ['Lebron', 'Tatum','Lillard', 'Embiid'],
        'Answer': 'Embiid',
    },
    {
        'Question': 'Which team had the best record in the last NBA season?',
        'Options': ['Milwalkee', 'Celtics','Denver', 'Memphis'],
        'Answer': 'Milwalkee',
    },
]

quantity_success = 0
for question in questions_base:
    print('Question:', question['Question'])
    print()

    options = question['Options']
    for i, option in enumerate(question['Options']):
        print(f'{i})', option)
    print()

    choice = input('Choose one option: ')

    success = False
    quantity_options = len(option)

    if choice == question['Answer']:
                success = True
    
    print()
    if success:
        os.system('cls')
        print('Right \o/')
        quantity_success += 1
    else:
        os.system('cls')
        print('Wrong :(')

print(f'You got it right {quantity_success} in {len(question)} questions')