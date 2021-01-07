import random
import emoji
# must install emoji package - 'pip3 install emoji'

#options = {1:'Rock',2:'Paper',3:'Scissors'}

# define items as emojis
rock = emoji.emojize(':gem_stone:')     # use until :rock: is available
paper = emoji.emojize(':roll_of_paper:')
scissors = emoji.emojize(':scissors:')

# add options to dictionary list
options = {1:rock, 2:paper, 3:scissors}

playerMove = 0
cpuInput = 0

playerScore = 0
cpuScore = 0

gameNumber = 0

print('Lets Play...\n')

# continue game until someone gets 5 wins
while not (playerScore == 5 or cpuScore == 5):
    # let player choice their option
    playerMove = int(input(f'(1) Rock {rock}, (2) Paper {paper}, (3) Scissors {scissors}\nEnter your choice: '))
    
    # prompt if wrong option entered
    if playerMove >= 4 or playerMove <= 0:
        print('Wrong option entered, try again.\n')
        continue

    # randominse CPU choice
    cpuMove = random.randint(1,3)

    gameNumber += 1

    print(f'\n--- GAME {gameNumber} ---')
    print(f'You: {options[playerMove]}')
    print(f'CPU: {options[cpuMove]}')

    # determine winner from each game by their choice
    if playerMove == 1 and cpuMove == 3:
        result = 'You WIN: Rock beats Scissors!\n'
        playerScore = playerScore + 1
    elif playerMove == 1 and cpuMove == 2:
        result = 'You LOSE: Paper beats Rock.\n'
        cpuScore = cpuScore + 1
    elif playerMove == 2 and cpuMove == 1:
        result = 'You WIN: Paper beats Rock!\n'
        playerScore = playerScore + 1
    elif playerMove == 2 and cpuMove == 3:
        result = 'You LOSE: Scissors beats Paper.\n'
        cpuScore = cpuScore + 1
    elif playerMove == 3 and cpuMove == 1:
        result = 'You LOSE: Rock beats Scissors.\n'
        cpuScore = cpuScore + 1
    elif playerMove == 3 and cpuMove == 2:
        result = 'You WIN: Scissors beats Paper!\n'
        playerScore = playerScore + 1
    else:
        result = "DRAW: both have the same!\n"

    print(f'{result}')

    print(f'Your score = {playerScore}')
    print(f'CPU score = {cpuScore}\n')

if playerScore == 5:
    print(f'You WON after {gameNumber} games - Congratulations!\n--- GAME OVER ---')
else:
    print(f'You LOST after {gameNumber} games - Better luck next time!\n--- GAME OVER ---')