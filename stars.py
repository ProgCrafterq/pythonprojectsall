# task 1
# num = int(input("Enter a number->"))
#
# num = abs(num)
# digits = 1
# while num > 9:
#     digits += 1
#     num //= 10
# print(f"Digits: {digits}")

# # task 2
# num = int(input("Enter a number->"))
#
# sum_val = 0
# while num > 0:
#     sum_val += num % 10
#     num //= 10
# print(f"Sum of digits: {sum_val}")

# # task 3.1
# num = int(input("Enter a number->"))
#
# counter = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         counter += 1
#
# if counter == 2:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# # task 3.2
# num = int(input("Enter a number->"))
#
# is_prime = True
# for i in range(2, int(num**0.5)+1):
#     if num % i == 0:
#         is_prime = False
#         break
#
# if is_prime:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# size = 5
#
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1 \
#                 or i == j or i + j == size - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# size = 5
#
# for i in range(size):
#     for j in range(size):
#         if i >= j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

for i in range(4):
    for j in range(7):
        if i + j >= 3 and i >= j - 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()
