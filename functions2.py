#
# def test_function():
#     print("Test 1,2,3")
#
#
# def print_range(num: int)->bool:
#     if num <= 0:
#         return False
#     for i in range(num):
#         print(i+1, end=" ")
#     print()
#     return True
#
# res = print_range(5)
# if res:
#     print("OK")
# else:
#     print("KO")


# def add(b: int):
#     b += 1
#     return b
#
# a = 5
# a = add(a)
# print(a)

# a = 5
# def add():
#     global a
#     a += 1
#     print(a)
#
#
# add()
# print(a)
#
# def print_list(lst: list[str]):
#     for i in lst:
#         print(i, end=" ")
#     print()
# #print_list(["1","2","3","4","5","6","7","8","9"])
#
# def list_dif(lst: list[int])->int:
#     result = 0
#     for i in lst:
#         result -= i
#     return result
# print(list_dif([1,2,3,4,5]))
#
# def zero_counter(lst: list[int])->int:
#     counter = 0
#     for item in lst:
#         if item == 0:
#             counter += 1
#     return counter
#
# l = [1,3,0,6,1,0,5]
# print(zero_counter(l))
# print(l.count(0))

# # task 1
#
# def list_sum(lst: list[int])->int:
#     s = 0
#     for item in lst:
#         s += item
#     return s
#
# print(list_sum([1,2,3,4,5]))
# print(list_sum([1,2,3]))


# def list_sum_prod(lst: list[int]):
#     s = 0
#     p = 1
#     for item in lst:
#         s += item
#         p *= item
#     return s,p
#
# s, p = list_sum_prod([1,2,3,4,5])
# print(s, p)

# task 5

def find_index(lst: list[int], val: int)->int:
    for i in range(len(lst)):
        if lst[i] == val:
            return i
    return -1

print(find_index([1,2,3,4,5],3))
print(find_index([1,2,3,4,5],13))

