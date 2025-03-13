import pickle

# with open("test.bin", "wb") as f:
#     pickle.dump("Hello", f)
#     pickle.dump(True, f)
#     pickle.dump(123.45, f)
#     pickle.dump(15, f)
#     pickle.dump([10,98,99,100,101], f)

# with open("test.bin", "rb") as f:
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))

import os

# os.mkdir("test_folder")
# os.rmdir("test_folder")

# for item in os.listdir():
#     if os.path.isdir(item):
#         print(f"<dir>\t{item}")
#     else:
#         print(f"<file>\t{item}")

# for item in filter(os.path.isfile,os.listdir()):
#     print(f"<file>\t{item}")

# print(os.path.exists("test.bin"))
# --------------------------------------------------

# day = int(input("Enter a day->"))
#
# match day:
#     case 3:
#         print("Wednesday")
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Error")


# 2  4 -> 2
# 3  5 -> 1
# 4  6 -> 2

# a = int(input("Enter first number->"))
# b = int(input("Enter second number->"))
#
# num = a if a < b else b
#
# # for i in range(1, num+1):
# #     if a % i == 0 and b % i == 0:
# #         gcd = i
# # print(f"GCD = {gcd}")
#
# for i in range(num, 0, -1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
#         break
# print(f"GCD = {gcd}")


# lst = list("hello")
# print(lst)
# # lst.pop(3)
# # lst.remove("l")
# # lst.clear()
# # del lst[3]
# # lst[3:4] = []
# print(lst)

# def test(*args):
#     print(args)
#
# test(1,2,3,4,5)
# test(1,2,3)
# test("Hello", "World")

# def test(**kwargs):
#     print(kwargs)
# 
# test(one = 1, two = 2, three = 3)