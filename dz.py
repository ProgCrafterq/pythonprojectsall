from random import randint

# TASK 1

# def find_neg(arr: list[int]) -> tuple[int, int]:
#     l, r = -1, -1
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             if l == -1:
#                 l = i
#             r = i
#     return l, r

# def bsort(arr: list[int]) -> list[int]:
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# lst = [10, -3, 5, -7, 2, 15, -1, 6, 8, -9, 4, -11, 20, -5, 12]
# l, r = find_neg(lst)
# if l != -1 and r != -1 and l < r:
#     lst[l + 1:r] = bsort(lst[l + 1:r])
# print("Список:", lst)

# TASK 2

def shuffle(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def bsort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def ssort(arr: list[int], desc: bool = False) -> list[int]:
    n = len(arr)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (arr[j] < arr[idx]) ^ desc:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

lst2 = [i for i in range(1, 21)]
lst2 = shuffle(lst2)
x = randint(1, 20)
pos = lst2.index(x)
lst2 = ssort(lst2[:pos], True) + [lst2[pos]] + bsort(lst2[pos + 1:])
print("ч:", x, "п:", pos)
print("список ==", lst2)
