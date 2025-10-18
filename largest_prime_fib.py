import argparse
from fibonacci_generator import generate_fibonacci

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_prime_fib(limit):
    """Find the largest prime Fibonacci number below 'limit'."""
    fibs = generate_fibonacci(limit)
    primes = [x for x in fibs if is_prime(x)]
    return max(primes) if primes else None

def main():
    parser = argparse.ArgumentParser(description="Find largest prime Fibonacci below a limit.")
    parser.add_argument("--limit", type=int, required=True, help="Upper limit for Fibonacci numbers")
    args = parser.parse_args()

    result = find_largest_prime_fib(args.limit)
    if result:
        print(f"The largest prime Fibonacci number less than {args.limit} is {result}.")
    else:
        print("No prime Fibonacci numbers found below that limit.")

if __name__ == "__main__":
    main()
