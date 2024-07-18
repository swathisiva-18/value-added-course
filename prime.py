def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_up_to(limit):
    print(f"Prime numbers up to {limit}:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

try:
    limit = int(input("Enter a number: "))
    print_primes_up_to(limit)
except ValueError:
    print("Please enter a valid integer.")
