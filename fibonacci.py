def fibonacci_series(limit):
    series = []
    a, b = 0, 1
    while a <= limit:
        series.append(a)
        a, b = b, a + b
    return series

def print_fibonacci_series(limit):
    series = fibonacci_series(limit)
    print(f"Fibonacci series up to {limit}:")
    for number in series:
        print(number, end=" ")
    print()

try:
    limit = int(input("Enter a number: "))
    print_fibonacci_series(limit)
except ValueError:
    print("Please enter a valid integer.")
