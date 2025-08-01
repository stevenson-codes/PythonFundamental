import random

def roll():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    player1 = input("Enter Player 1:\n")
    player2 = input("Enter Player 2:\n")

    roll1 = roll()
    roll2 = roll()

    print(f'{player1} rolled {roll1}')
    print(f'{player2} rolled {roll2}')

    if roll1 > roll2:
        print(f'{player1} wins!')
    elif roll1 < roll2:
        print(f'{player2} wins!')
    else:
        print('tie!')

main()