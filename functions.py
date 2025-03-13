# from random import randint as rand
# lst1 = [i for i in range(10)]
# print(lst1)
# lst2 = [rand(-10,10) for i in range(10)]
# print(lst2)
#
# positive_numbers = sum([1 for i in lst2 if i > 0])
# print(positive_numbers)

#
# def hello(quantity: int = 1):
#     for i in range(quantity):
#         print("Hello world!!!")
#
#
# def my_sum(a: int, b: int) -> int:
#     return a + b
#
#
# def words_counter(line: str) -> int:
#     return len(line.split())
#
#
# print(words_counter("one two three four five"))
# hello(5)
# print()
# hello(3)
# print()
# hello()

# res = my_sum(b=23, a=12)*5
# print(type(res))
# res = hello()
# print(type(res))


# # task 1
#
# def print_quot():
#     print("\"Don't let the noise of others' opinions\ndrown"
#           " out your own inner voice.\"\n\033[93mSteve Jobs")
#
#
# print_quot()
import random


# # task 2
#
# def print_odd_numbers(start: int, end: int):
#     if start > end:
#         start, end = end, start
#     for i in range(start, end):
#         if i % 2 != 0:
#             print(i, end=" ")
#     print()
#
#
#
# print_odd_numbers(random.randint(0,20),random.randint(0,20))

# task 3

def draw_line(length: int, symbol: str = "*", direction: str = "h"):
    for i in range(length):
        if direction == "h":
            print(symbol, end="")
        elif direction == "v":
            print(symbol)
        else:
            print("Error")
            break
    print()



draw_line(10, "!", "h")
draw_line(5)
