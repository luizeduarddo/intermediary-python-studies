#Exercise of Questions and Answers using NBA events.
import os

questions_base = [
    {
        'Question': 'Which Team won the last NBA Finals?',
        'Options': ['Miami', 'Denver','Celtics', 'Brooklyn'],
        'Answer': 1,
    },
    {
        'Question': 'Who was the MVP in the the last NBA season?',
        'Options': ['Lebron', 'Tatum','Lillard', 'Embiid'],
        'Answer': 3,
    },
    {
        'Question': 'Which team had the best record in the last NBA season?',
        'Options': ['Milwalkee', 'Celtics','Denver', 'Memphis'],
        'Answer': 0,
    },
]

quantity_success = 0
for question in questions_base:
    print('Question:', question['Question'])
    print()

    options = question['Options']
    for i, option in enumerate(options):
        print(f'{i})', option)
    print()

    choice = int(input('Choose one option by index number: '))

    success = False
    quantity_options = len(option)

    if choice == question['Answer']:
        success = True
    
    if success:
        os.system('cls')
        print('Right \o/')
        quantity_success += 1
    else:
        os.system('cls')
        print('Wrong! :(')
os.system('cls')

print(f'You got it right {quantity_success} in {len(question)} questions')