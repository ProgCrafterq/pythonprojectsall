# print("\033[95mHello \033[92mworld")
# print("\\Hello\\\n\t\"world\"")


# name = input("Enter your name->")
# print("Hello", name)
#
# a = int(input("Enter first number->"))
# b = int(input("Enter second number->"))
# print(type(a))
# print(type(b))
# print(a+b)

# a+b
# a-b
# a*b
# a/b
# a//b
# a%b
# a**b

# # task 1.1
#
# a = int(input("Enter first number->"))
# b = int(input("Enter second number->"))
#
# sum = a + b
# dif = a - b
# prod = a * b
#
# print(f"Sum = {sum}")
# print(f"Dif = {dif}")
# print(f"Prod = {prod}")

# #task 1.2
#
# num = int(input("Enter a number->"))
# percent = int(input("Enter the percent->"))
# result = num / 100 * percent
# print(f"{percent}% of {num} is {result}")

# # task 2.1
#
# num = int(input("Enter a two-digit number->"))
#
# units = num % 10
# tens = num // 10
#
# print(f"{tens}\n{units}")

# task 2.2

num = int(input("Enter a three-digit number->"))

units = num % 10
tens = num // 10 % 10
hundreds = num // 100

print(f"{hundreds} {tens} {units}")
print(f"Sum = {hundreds+tens+units}")
