import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Introduction message
    print("Welcome to the Guess the Number Game!")
    print("I have generated a random number between 1 and 100.")
    print("Your task is to guess it.")
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        # Prompt the user to input their guess
        user_guess = input("Enter your guess: ")
        
        # Make sure the input is a valid number
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        # Convert the input into an integer
        user_guess = int(user_guess)
        attempts += 1
        
        # Compare the user's guess to the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
            break

# Start the game
guess_the_number()
