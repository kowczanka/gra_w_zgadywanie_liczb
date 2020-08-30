from random import randint

def zgadywanka():
    number_to_guess = randint(1,100)
    guessed = False
    while not guessed:
        number = input("Guess a number from 1 to 100: ")
        try:
            number = int(number)
        except ValueError:
            print("This is not a number!")
            continue

        if number > number_to_guess:
            print("To big!")
        elif number < number_to_guess:
            print("To small!")
        else:
            print("You win!")
            return

zgadywanka()
