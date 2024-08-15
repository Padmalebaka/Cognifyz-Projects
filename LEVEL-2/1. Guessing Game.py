import random

def main():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    
    print("Guess the Number Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        # Prompt the user to enter a guess
        try:
            guess = int(input("Enter your guess: "))
            
            # Provide feedback on the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number: {number_to_guess}.")
        except ValueError:
            print("Please enter a valid number.")
            
if __name__ == "__main__":
    main()