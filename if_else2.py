# a = int(input("Enter first number->"))
# b = int(input("Enter second number->"))
# c = int(input("Enter third number->"))
# # if a < b and a < c:
# #     print(a)
# # elif b < c:
# #     print(b)
# # else:
# #     print(c)
#
# min_value = a
# if b < min_value:
#     min_value = b
# if c < min_value:
#     min_value = c
# print(min_value)

# # task 1
# num = int(input("Enter 6-digit number->"))
# num = abs(num) #num if num > 0 else -num
# if num >= 100000 and num < 1000000:
#     d6 = num % 10
#     d5 = num // 10 % 10
#     d4 = num // 100 % 10
#     d3 = num // 1000 % 10
#     d2 = num // 10000 % 10
#     d1 = num // 100000
#     if d1 + d2 + d3 == d4 + d5 + d6:
#         print(f"{num} is a lucky number")
#     else:
#         print(f"{num} is not a lucky number")
# else:
#     print("Error. Wrong number")

#
# # task 2
# num = int(input("Enter 6-digit number->"))
# if num >= 100000 and num < 1000000:
#     d6 = num % 10
#     d5 = num // 10 % 10
#     d4 = num // 100 % 10
#     d3 = num // 1000 % 10
#     d2 = num // 10000 % 10
#     d1 = num // 100000
#     res = d6*100000+d5*10000+d3*1000+d4*100+d2*10+d1
#     print(res)
# else:
#     print("Error. Wrong number")

# # task 3
#
# month = int(input("Enter a month->"))
#
# if month == 1 or month == 2 or month == 12:
#     print("Winter")
# elif month >= 3 and month <= 5:
#     print("Spring")
# elif month >= 6 and month <= 8:
#     print("Summer")
# elif month >= 9 and month <= 11:
#     print("Autumn")
# else:
#     print("Error. Wrong month")

# task 4
# seconds = int(input("Enter a number of seconds->"))
# seconds = 86400 - seconds
# choice = input("Enter (h/m/s) to convert->")
# if choice == "h":
#     print(f"{seconds/3600}h")
# elif choice == "m":
#     print(f"{seconds / 60}m")
# elif choice == "s":
#     print(f"{seconds}s")
# else:
#     print("Error")

# def find_nsk(a: int, b: int) -> int:
#     i = a * b
#     while i >= a and i >= b:
#         if i % a == 0 and i % b == 0:
#             return i
#         i -= 1

# num1 = int(input("Введіть 1 число: "))
# num2 = int(input("Введіть 2 число: "))

# lcd = find_nsk(num1, num2)

# print(f"Найменше спільне кратне чисел {num1} та {num2} = {lcd}")




# def find_nsk(a: int, b: int) -> int:
#     if a > b:
#         start = a
#     else:
#         start = b

#     for i in range(start, a * b + 1):
#         if i % a == 0 and i % b == 0:
#             return i

# num1 = int(input("Введіть 1 число: "))
# num2 = int(input("Введіть 2 число: "))

# nsk = find_nsk(num1, num2)

# print(f"Найменше спільне кратне чисел {num1} та {num2} = {nsk}")

