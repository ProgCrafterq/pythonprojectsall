# Task 1
def print_digits(n: int):
    if n < 10:
        print(n, end=' ')
    else:
        print_digits(n // 10)
        print(n % 10, end=' ')

print_digits(12345)
print("\n")

# Task 2
def sum_range(min_val: int, max_val: int) -> int:
    if min_val > max_val:
        return 0
    return min_val + sum_range(min_val + 1, max_val)

print(sum_range(2, 5))
print("\n")

# Task 3
def fibonacci_sum(n: int, a: int = 0, b: int = 1) -> int:
    if n == 0:
        return 0
    if n == 1:
        return a
    return a + fibonacci_sum(n - 1, b, a + b)

print(fibonacci_sum(5))
print("\n")

# Task 4
def fibonacci_series(n: int, a: int = 0, b: int = 1):
    if n > 0:
        print(a, end=' ')
        fibonacci_series(n - 1, b, a + b)

fibonacci_series(7)
print("\n")
