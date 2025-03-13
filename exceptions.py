from random import randint as rand


# from time import time
#
# def quick_sort(lst: list):
#     if len(lst) <= 1:
#         return lst
#     tmp = lst[0]
#     left_part = [item for item in lst[1:] if item <= tmp]
#     right_part = [item for item in lst[1:] if item > tmp]
#     return quick_sort(left_part) + [tmp] + quick_sort(right_part)
#
#
# def selection_sort(lst: list[int]):
#     for i in range(len(lst)):
#         min_pos = i
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[min_pos]:
#                 min_pos = j
#         lst[i], lst[min_pos] = lst[min_pos], lst[i]
#
#
# lst = [rand(0, 10000) for item in range(100000)]
# start = time()
# quick_sort_lst = quick_sort(lst)
# end = time()
# print(f"Quick sort: {end-start: 0.6f}")
#
# start = time()
# sorted_lst = sorted(lst)
# end = time()
# print(f"Tim sort: {end-start: 0.6f}")
# #print(quick_sort_lst)
# # start = time()
# # selection_sort(lst)
# # end = time()
# # print(f"Selection sort: {end-start: 0.6f}")
# #print(lst)
#

# lst = [rand(-10, 10) for item in range(10)]
# print(lst)

# res_lst = []
# for i in lst:
#     res_lst.append(i*10)

# res_lst = [i*10 for i in lst]
# from functools import reduce
#
# res_lst = list(map(lambda item: item * 10, lst))
# print(res_lst)
#
# even_lst = list(filter(lambda item: item % 2 == 0, lst))
# print(even_lst)
#
# s = reduce(lambda a,b:a+b,lst)
# print(s)
# s = sum(lst)
# print(s)


# ~~~~~~~~~~~~~~~~~~~~ Exceptions ~~~~~~~~~~~~~~~~~~

#
# try:
#     a = int(input("Enter first number->"))
#     b = int(input("Enter second number->"))
#     if a < 0:
#         raise Exception("My message about an error")
#     res = a / b
# except ZeroDivisionError as ex:
#     print(f"Cannot divide by zero. {ex}")
# except ValueError as ex:
#     print(f"Value error: {ex}")
# except Exception as ex:
#     print(f"Exception: {ex}")
# else:
#     print(f"Result = {res}")
# finally:
#     print("Finally part")
#
# print("End of program")


# def div(a: int, b: int) -> float:
#     return a / b
#
#
# a = int(input("Enter first number->"))
# b = int(input("Enter second number->"))
# try:
#     res = div(a, b)
#     print(res)
# except:
#     print("Error")


# # task 2.1
#
# def div(a,b):
#     print(a/b)
#
# try:
#     div(12,0)
# except:
#     print("Error")

# task 2.2

def div(a,b):
    try:
        print(a / b)
    except:
        print("Error")

div(12,0)
