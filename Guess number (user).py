#It's program where user suppose to have in mind his number and computers tries to guess it. Put small "h" if number is too high or "s" if too small or "c: if correct
import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high, too low or correct')
        if feedback == 'h':
            high == guess - 1
        elif feedback == 'l':
            low = guess +1
    print (f'Yay you guessed {guess} right')



computer_guess(10)
