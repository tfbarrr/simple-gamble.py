import random

while True:
    choice = input('Do you want to gamble? (y/n): '). lower()
    player1 = random.randint(0, 36)
    player2 = random.randint(0, 36)
    
    if player1 > player2:
        winner = 'You'
        win_pts = player1
        loser = 'Bot'
        lose_pts = player2
    else:
        winner = 'Bot'
        win_pts = player2
        loser = 'You'
        lose_pts = player1
    if choice == 'y':
        print(f'(Win: {winner}, {win_pts})')
        print(f'(Lose: {loser}, {lose_pts})')
    elif choice == 'n':
        print('bye noobie')
        break
    else:
        print('invalid input')
    