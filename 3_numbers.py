import random


def generate_numbers(n):
    # Ensure n is at least 3
    if n < 3:
        raise ValueError("n must be at least 3")
    
    # Generate two random numbers a and b such that a < b < n/2
    a = random.randint(1, n - 2)
    b = random.randint(a + 1, n - 1)
    
    # Calculate the third number c such that a + b + c = n
    c = n - a - b
    
    # Ensure c is distinct from a and b
    while c in (a, b) or c < 0:
        # If c is equal to a or b, regenerate a and b
        a = random.randint(1, n - 2)
        b = random.randint(a + 1, n - 1)
        c = n - a - b
    
    return a, b, c


def main():
    n = int(input("Enter a number: "))
    a, b, c = generate_numbers(n)
    print(f"For n = {n}, the numbers are {a}, {b}, and {c}")


main()
