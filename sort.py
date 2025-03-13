# def change_var(val: int):
#     val += 1
#
# val = 0
# change_var(val)
# print(val)

# def change_lst(lst: list[int]):
#     lst.append(1)
#
# l = []
# change_lst(l)
# print(l)
import time
from random import randint as rand

def linear_search(lst: list[int], val: int) -> int:
    for i in range(len(lst)):
        if lst[i] == val:
            return i
    return -1


def binary_search(lst: list[int], val: int) -> int:
    lb = 0
    rb = len(lst) - 1
    while lb < rb:
        pos = (lb + rb) // 2
        if lst[pos] == val:
            return pos
        if lst[pos] < val:
            lb = pos + 1
        else:
            rb = pos - 1
    return -1


def bubble_sort(lst: list[int]):
    for i in range(len(lst)):
        for j in range(len(lst) - 1, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]

def selection_sort(lst: list[int]):
    for i in range(len(lst)):
        min_pos = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_pos]:
                min_pos = j
        lst[i], lst[min_pos] = lst[min_pos], lst[i]
#lst = [34, 1, 65, 34, 12, 68, 54]
lst = [rand(0,10000) for _ in range(10000)]
#print(lst)
start_time = time.time()
bubble_sort(lst)
end_time = time.time()
#print(lst)
print(f"bubble sort: {end_time - start_time: .6f}")
#lst = [34, 1, 65, 34, 12, 68, 54]
lst = [rand(0,10000) for _ in range(10000)]
#print(lst)
start_time = time.time()
selection_sort(lst)
end_time = time.time()
#print(lst)
print(f"selection sort: {end_time - start_time: .6f}")
#print(linear_search(lst, 65))
#print(binary_search(lst, 65))
