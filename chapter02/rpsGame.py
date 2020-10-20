import sys
import random

wins = 0
loses = 0
ties = 0

while True:
    print('%s Wins, %s Loses, %s Ties'%(wins, loses, ties))

    while True:
        print('Enter your move: r(Rock), p(Paper), s(Scissors)')
        playerMove = input()

        if playerMove == 'q':
            sys.exit()
        if playerMove in ['r', 'p', 's']:
            break
        print('Type one of r, p, s, q')

    if playerMove == 'r':
        print('Rock vs ..')
    elif playerMove == 'p':
        print('Paper vs ..')
    else:
        print('Scissors vs ..')

    randomMove = random.randint(1, 3)

    if randomMove == 1:
        computerMove = 'r'
        print('Rock')
    elif randomMove == 2:
        computerMove = 'p'
        print('Paper')
    else:
        computerMove = 's'
        print('Scissors')

    if playerMove == computerMove:
        print('It is a draw')
        ties = ties + 1
    elif( (playerMove == 'r' and computerMove == 'p')
          or (playerMove == 'p' and computerMove == 's') or (playerMove == 's' and computerMove == 'r')):
        loses = loses + 1
        print('You lose!')
    else:
        wins = wins + 1
        print('You won!')

