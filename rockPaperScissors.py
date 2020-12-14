import random

rock = 1
paper = 2
scissors = 3

userMove = 0
cpuInput = 0

userScore = 0
cpuScore = 0

print('Lets Play...\n')

while userScore <= 4 or cpuScore <= 4:
    # print('Lets Play...\n')
    print('Your score = ' + str(userScore))
    print('CPU score = ' + str(cpuScore) + '\n')
    userMove = int(input("(1) Rock, (2) Paper, (3) Scissors\nEnter your choice: "))
    #print(userInput)
    cpuMove = random.randint(1,3)

    if userMove == 1 and cpuMove == 3:
        print('You WIN: Rock beats Scissors!\n')
        userScore = userScore + 1
    elif userMove == 1 and cpuMove == 2:
        print('You LOSE: Paper beats Rock.\n')
        cpuScore = cpuScore + 1
    elif userMove == 2 and cpuMove == 1:
        print('You WIN: Paper beats Rock!\n')
        userScore = userScore + 1
    elif userMove == 2 and cpuMove == 3:
        print('You LOSE: Scissors beats Paper.\n')
        cpuScore = cpuScore + 1
    elif userMove == 3 and cpuMove == 1:
        print('You LOSE: Rock beats Scissors.\n')
        cpuScore = cpuScore + 1
    elif userMove == 3 and cpuMove == 2:
        print('You WIN: Scissors beats Paper!\n')
        userScore = userScore + 1
    else:
        print("DRAW: both have the same!\n")

