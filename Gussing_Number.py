import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guess = None
    
    # Keep asking until the user guesses correctly
    while guess != number_to_guess:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Correct! The number was {number_to_guess}. It took you {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

# Call the function to start the game
guess_the_number()