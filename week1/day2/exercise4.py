import random

# First version
def get_single_guess():
    secret_num = random.randint(1, 100)
    user_guess = input('Please guess the number: ')
    # Convert it to an int
    user_num = int(user_guess)
    if user_num == secret_num:
        print('You guessed it!')
    else:
        print('You are the weakest link. Goodbye! (The number was {})'
            .format(secret_num))


# Second version - allow the user to guess multiple times
def get_multiple_guesses():
    # Don't put this inside the loop! Otherwise every time
    # you ask the user to guess, the secret number will
    # have changed.
    secret_num = random.randint(1, 100)
    # We have only learned 'for' loops so far, so we'll allow 100 guesses
    for i in range(100):
        user_guess = input('Please guess the number: ')
        # Convert it to an int
        user_num = int(user_guess)
        if user_num == secret_num:
            print('You guessed it!')
            # Stop the loop right away
            break
        else:
            message = 'Nope. Please try again. '
            if secret_num > user_num:
                message += '(The secret number is HIGHER)'
            else:
                message += '(The secret number is LOWER)'
            print(message)


# Uncomment whichever version you want to run
# get_single_guess()
# get_multiple_guesses()
