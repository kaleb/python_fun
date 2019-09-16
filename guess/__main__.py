import sys

games_played = 0
guesses = 0

def guess(min: int, max: int, count: int):
    half = (min + max) // 2
    answer = input(f'{half}? ')
    if answer not in ['h', 'l', 'c']:
        print('responses must be h for higher, l for lower, or c for correct. Goodbye.')
        return guess(min, max, count)
    if answer == 'c':
        return half, count
    if min == max:
        sys.exit("That's not correct.")
    if answer == 'h':
        return guess(half + 1, max, count + 1)
    if answer == 'l':
        return guess(min, half - 1, count + 1)


if __name__ == '__main__':
    n = input('Please enter a number n: ')

    try:
        n = int(n)
    except:
        sys.exit('n must be an integer')
    if n <= 0:
        sys.exit('n must be greater than zero')

    while True:
        games_played += 1
        answer, count = guess(1, n, 1)
        print(f'Your number is {answer}')
        print(f'It took me {count} guesses')
        guesses += count
        print(f'I averaged {guesses/games_played} guesses per game for {games_played} game(s)')
        while True:
            yesno = input('Play again? (y/n) ')
            if yesno == 'n':
                sys.exit(0)
            if yesno == 'y':
                break