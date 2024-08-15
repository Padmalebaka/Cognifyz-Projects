import random

def main():
    print("Welcome to the Number Guessing Game!")
    
    # Prompt the user to specify the range for the random number
    try:
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))
        
        # Ensure the upper bound is greater than the lower bound
        if lower_bound >= upper_bound:
            print("The upper bound must be greater than the lower bound. Please restart the game.")
            return
    except ValueError:
        print("Please enter valid integers for the range.")
        return
    
    # Generate a random number within the specified range
    number_to_guess = random.randint(lower_bound, upper_bound)
    guess = None
    
    print(f"I have chosen a number between {lower_bound} and {upper_bound}. Can you guess it?")
    
    # Loop until the user guesses the correct number
    while guess != number_to_guess:
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