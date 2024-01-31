import random


def riemann(f, a, b, n):
    interval = (b - a) / n

    area = 0
    for i in range(0, n):
        middle = ((a + i * interval) + (a + (i + 1) * interval)) / 2
        area += f(middle) * interval

    return area


def f(x):
    y = x ** 2 + 2
    return y


def g(x):
    y = x
    return y


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
    print("1 - Calculate integral of x^2 + 2 from 1 to 2 with n subintervals\n")
    n = int(input("Enter the number of subintervals: "))
    lim_inf = 1
    lim_sup = 2
    area = riemann(f, lim_inf, lim_sup, n)
    print("The area under the curve of f(x) = x^2 + 2 is approximately {:.4}\n".format(area))

    print("2 - Calculate the area between x^2 + 2 and x from 1 to 2\n")
    lim_inf = 1
    lim_sup = 2
    area2 = riemann(g, lim_inf, lim_sup, n)
    print("The area between f(x) = x^2 + 2 and g(x) = x is approximately {:.4}\n".format(area - area2))

    print("3 - Given a number n, produce 3 distinct numbers that their sum is equal to n\n")
    n = int(input("Enter a number (greater than 2): "))
    a, b, c = generate_numbers(n)
    print(f"For n = {n}, the numbers are {a}, {b}, and {c}")


main()
