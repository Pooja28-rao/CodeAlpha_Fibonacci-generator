# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

# Input: Number of terms you want in the Fibonacci sequence
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generating and printing the Fibonacci sequence
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence: [0]")
else:
    print(f"Fibonacci sequence: {fibonacci(n)}")