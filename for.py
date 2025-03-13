# a = int(input("Enter first number->"))
# b = int(input("Enter second number->"))
#
# max_value = a if a > b else b
#
# # if a > b:
# #     max_value = a
# # else:
# #     max_value = b
#
# print(f"Max value = {max_value}")

# a = int(input("Enter first number->"))
# b = int(input("Enter second number->"))
#
# print(f"{a} -> {b}")
# # tmp = a
# # a = b
# # b = tmp
# a, b = b, a
# print(f"{a} -> {b}")


# # 2024 - a leap year
# # 2023 - not a leap year
# # 2000 - a leap year
# # 2100 - not a leap year
#
# year = int(input("Enter a year->"))
#
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# a = 3
# b = 0
#
# if b != 0 and a % b == 0:
#     print("True")
# else:
#     print("False")


#~~~~~~~~~~ loops ~~~~~~~~~~~~
# for, while


# for i in range(10):
#     print("Hello world")

# for i in range(1, 11, 2):
#     print(i, end=" ")
# print()

# for i in range(10, -1, -2):
#     print(i, end=" ")
# print()

# # task 1
# start = int(input("Enter the start of the range->"))
# finish = int(input("Enter the finish of the range->"))
#
# for number in range(start, finish):
#     print(number, end=" ")
# print()

# # task 2
# start = int(input("Enter the start of the range->"))
# finish = int(input("Enter the finish of the range->"))
#
# for number in range(start, finish):
#     if number % 2 != 0:
#         print(number, end=" ")
# print()

# # task 4
# start = int(input("Enter the start of the range->"))
# finish = int(input("Enter the finish of the range->"))
#
# for num in range(finish, start, -1):
#     print(num, end=" ")
# print()

# # task 5
# start = int(input("Enter the start of the range->"))
# finish = int(input("Enter the finish of the range->"))
# 
# if start > finish:
#     start, finish = finish, start
# 
# for num in range(start, finish):
#     if num % 2 != 0:
#         print(num, end=" ")
# print()