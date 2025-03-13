# def add(*args):
#     print(type(args))
#     s = 0
#     for item in args:
#         s += item
#     return s
#
# def find_min_max(*args):
#     min_val = args[0]
#     max_val = args[0]
#     for item in args:
#         if min_val > item:
#             min_val = item
#         if max_val < item:
#             max_val = item
#     return min_val, max_val
#
# min_val, max_val = find_min_max(12, 23,1,2,3,4)
# print(min_val, max_val)
# print(find_min_max(12, 23))
# print(find_min_max(12, 23,1))
# print(find_min_max(3,4))
# print(add(12, 23,1,2,3,4))
# print(add(12, 23))
# print(add(12, 23,1))
# print(add(3,4))


# nums = (1,2,3,4,5,6)
# print(nums)
# a,b,c,*d = nums
# print(a,b,c,d)

#
# def print_person(f_name, l_name, *args, age = 1):
#     print(f"First name: {f_name}")
#     print(f"Last name: {l_name}")
#     print(f"Age: {age}")
#     print("Misc: ")
#     for i in args:
#         print(f"\t\t{i}")
#
# print_person("Vasya", "Pupkin", age=12)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def factorial_i(num: int)->int:
#     f = 1
#     for i in range(1, num+1):
#         f *= i
#     return f

# def factorial_r(num: int)->int:
#     if num < 2:
#         return 1
#     return num * factorial_r(num - 1)
#
# print(factorial_r(3))
# print(factorial_r(5))
# print(factorial_i(3))
# print(factorial_i(5))

# def digits_counter(num: int)->int:
#     if num < 10:
#         return 1
#     return 1 + digits_counter(num // 10)
#
# print(digits_counter(123))
# print(digits_counter(44))

# def sum_digits(num: int)->int:
#    if num < 10:
#        return num
#    return num % 10 + sum_digits(num // 10)
#
# print(sum_digits(123))
# print(sum_digits(44))

# def print_digits(num: int):
#     if num < 10:
#         print(num, end=" ")
#     else:
#         print(num % 10, end=" ")
#         print_digits(num // 10)
#
#
# print_digits(123)
# print()
# print_digits(24687531)

# 0 1 2 3 4 5 6 7  8  9  10
# 0 1 1 2 3 5 8 13 21 34 55

def fib_num(num: int)->int:
    if num < 2:
        return num
    return fib_num(num-1) + fib_num(num-2)

def fib_num_fast(num:int, a:int=0, b:int=1)->int:
    if num == 0:
        return a
    return fib_num_fast(num-1, b, a+b)

print(fib_num_fast(100))
#print(fib_num(37))
