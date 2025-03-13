# Task 1 exceptonu dz3.txt
try:
    name: str = input("E name: ")
    age: int = int(input("E age: "))
    if age < 0 or age > 130:
        raise ValueError("incorrect age")
    print(f"Привіт, {name}! Твій вік — {age}")
except ValueError as e:
    print("error", e)

# Task 2 - Version 1
def greeting_v1(name: str, age: int) -> str:
    if age < 0 or age > 130:
        raise ValueError("incorrect age!!!")
    return f"Привіт, {name}! Твій вік — {age}"

try:
    name: str = input("E name: ")
    age: int = int(input("E age: "))
    print(greeting_v1(name, age))
except ValueError as e:
    print("error", e)

# Task 2 - Version 2
def greeting_v2(name: str, age: int) -> str:
    try:
        if age < 0 or age > 130:
            raise ValueError("incorrect age")
        return f"Привіт, {name}! Твій вік — {age}"
    except ValueError as e:
        return f"error {e}"

name: str = input("E name: ")
age: int = int(input("E age: "))
print(greeting_v2(name, age))

# Task 3
try:
    numbers: list[float] = []
    n: int = int(input("enter num of numers: "))
    for i in range(n):
        num: float = float(input("enter numer: "))
        if num <= 0:
            raise ValueError("typed negative number")
        numbers.append(num)
    print("Sum:", sum(numbers))
except ValueError as e:
    print("error", e)


# Task 4 - Version 1
def sum_positive_v1(numbers: list[float]) -> float:
    for num in numbers:
        if num <= 0:
            raise ValueError("list contains negative mumber")
    return sum(numbers)

try:
    numbers_input: list[float] = [float(x) for x in input("enter numers: ").split()]
    print("Sum:", sum_positive_v1(numbers_input))
except ValueError as e:
    print("error", e)

# Task 4 - Version 2
def sum_positive_v2(numbers: list[float]) -> float:
    try:
        for num in numbers:
            if num <= 0:
                raise ValueError("list contains negative mumber")
        return sum(numbers)
    except ValueError as e:
        print("error", e)
        return 0.0

numbers_input: list[float] = [float(x) for x in input("enter numers ").split()]
print("Sum:", sum_positive_v2(numbers_input))

