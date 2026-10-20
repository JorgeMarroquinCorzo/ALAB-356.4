# fibonacci_generator.py
#series of numbers in which each number (Fibonacci number)
#  is the sum of the two preceding ones, usually starting with 0 and 1.

def gen_fibonacci(n):
    """Yield the first n numbers of the Fibonacci sequence (0, 1, 1, 2, 3, 5, ...)."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    count = 10
    print(f"First {count} Fibonacci numbers:")
    for i, number in enumerate(gen_fibonacci(count), start=1):
        print(f"Fibonacci #{i}: {number}")