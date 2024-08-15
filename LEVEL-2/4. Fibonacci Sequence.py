def generate_fibonacci(n):
    # Initialize the first two terms of the Fibonacci sequence
    fib_sequence = []
    
    if n >= 1:
        fib_sequence.append(0)  # First term
    if n >= 2:
        fib_sequence.append(1)  # Second term
    
    # Generate the Fibonacci sequence up to n terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

def main():
    # Prompt the user to enter the number of terms
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence = generate_fibonacci(n)
            print(f"The Fibonacci sequence up to {n} terms is:")
            print(fibonacci_sequence)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()