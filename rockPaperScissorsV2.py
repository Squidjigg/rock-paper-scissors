import random

#rock = 1
#paper = 2
#scissors = 3
options = {1:'Rock',2:'Paper',3:'Scissors'}

#print(options[1])

userMove = 0
cpuInput = 0

userScore = 0
cpuScore = 0

print('Lets Play...\n')

while not (userScore == 5 or cpuScore == 5):
    # print('Lets Play...\n')

    userMove = int(input('(1) Rock, (2) Paper, (3) Scissors\nEnter your choice: '))

    #print(userInput)
    cpuMove = random.randint(1,3)

    print(f'You: {options[userMove]}')
    print(f'CPU: {options[cpuMove]}')

    if userMove == 1 and cpuMove == 3:
        result = 'You WIN: Rock beats Scissors!\n'
        userScore = userScore + 1
    elif userMove == 1 and cpuMove == 2:
        result = 'You LOSE: Paper beats Rock.\n'
        cpuScore = cpuScore + 1
    elif userMove == 2 and cpuMove == 1:
        result = 'You WIN: Paper beats Rock!\n'
        userScore = userScore + 1
    elif userMove == 2 and cpuMove == 3:
        result = 'You LOSE: Scissors beats Paper.\n'
        cpuScore = cpuScore + 1
    elif userMove == 3 and cpuMove == 1:
        result = 'You LOSE: Rock beats Scissors.\n'
        cpuScore = cpuScore + 1
    elif userMove == 3 and cpuMove == 2:
        result = 'You WIN: Scissors beats Paper!\n'
        userScore = userScore + 1
    else:
        result = "DRAW: both have the same!\n"

    print(f'{result}')

    print(f'Your score = {userScore}')
    print(f'CPU score = {cpuScore}\n')
