# print("Something")
# var = input("Enter something ->")
# print(var)

# +, -, *, //, %, /, **
# import math
# print(math.cos(0))

# ==, !=, >, <, >=, <=
# and, or, not

#
# # 24554
# num = int(input("Enter a number->"))
#
# sum_digits = 0
#
# while num != 0:
#     digit = num % 10
#     sum_digits += digit
#     num //= 10
#
# print(f"Sum of digits is {sum_digits}")

# a = "Hello"
# b = a[:]
# print(id(a))
# print(id(b))
from random import randint as rand

#
# lst = []
#
# for i in range(10):
#     lst.append(rand(0,10))
#
# print(len(lst))
# print(lst)
# # even numbers
# even_counter = 0
#
# for item in lst:
#     if item % 2 == 0:
#         even_counter += 1
# print(f"Quantity of even numbers is {even_counter}")

# unique numbers
lst = []

for i in range(10):
    lst.append(rand(0, 10))

print(len(lst))
print(lst)

# # 1
# unique_list = []
# for item in lst:
#     if item not in unique_list:
#         unique_list.append(item)
# print(f"Quantity of unique numbers is {len(unique_list)}")

# # 2
# unique_counter = 0
# for i in range(len(lst)):
#     if lst[i] not in lst[:i]:
#         unique_counter += 1
# print(f"Quantity of unique numbers is {unique_counter}")

# # 3
#
#
# unique_counter = 0
# for item in lst:
#     if lst.count(item)==1:
#         unique_counter += 1
# print(f"Quantity of unique numbers is {unique_counter}")
#
# # 4
# unique_counter = 1
# lst.sort()
# print(lst)
# for i in range(1, len(lst)):
#     if lst[i] != lst[i - 1]:
#         unique_counter += 1
# print(f"Quantity of unique numbers is {unique_counter}")
