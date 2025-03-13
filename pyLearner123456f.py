# Taskk1

# def product_of_list(lst: list[int]) -> int:
#     result = 1
#     for num in lst:
#         result *= num
#     return result
# print(product_of_list([2, 3, 4, 5]))  



# Tassk2

# def min_of_list(lst: list[int]) -> int:
#     minimum = lst[0]
#     for num in lst[1:]:
#         if num < minimum:
#             minimum = num
#     return minimum

# print(min_of_list([5, 2, 8, 1, 9]))  




# Task 3
# def count_prost(numbers):
#     def is_prost(q):
#         if q < 2:
#             return False
#         for i in range(2, int(q ** 0.5) + 1):
#             if q % i == 0:
#                 return False
#         return True

#     count = 0
#     for num in numbers:
#         if is_prost(num):
#             count += 1
#     return count


# print(count_prost([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) 




# Task 4
# def remove_number(lst, num):
#     count = 0  
#     i = 0  
    
#     while i < len(lst):  
#         if lst[i] == num:  
#             del lst[i]  
#             count += 1  
#         else:
#             i += 1  
    
#     return count  

# numbers = [1, 2, 3, 4, 2, 5, 2, 6]
# deleted_count = remove_number(numbers, 2)
# print("Кількість вид ел:", deleted_count)
# print("Оновлений список:", numbers)






#Task 5


# def merge_lists(l1, l2):
#     merged_list = []  
    
#     for item in l1:
#         merged_list.append(item)
    
#     for item in l2:
#         merged_list.append(item)
    
#     return merged_list  

# li_1 = [1, 2, 3, 4]
# li_2 = [5, 6, 7, 8]
# result = merge_lists(li_1, li_2)

# print("Об'єднаний список:", result)




#Task 6

# def st_list(lst, st):
#     result_list = [] 

#     for item in lst:
#         stypin_value = item ** st 
#         result_list.append(stypin_value)  
    
#     return result_list  

# numbers = [2, 3, 4, 5]
# st = 3
# result = st_list(numbers, st)

# print("Результат піднесення до ступеня:", result)




# def counter_digits(n):
#     if n == 0:
#         return 1  

#     if n < 10:
#         return 1

#     new_number_d = n // 10  

#     result = counter_digits(new_number_d) + 1

#     return result

# print(counter_digits(2025)) 



# def sum_digits(n):
#     if n == 0:
#         return 0  

#     last_digit = n % 10
#     new_number = n // 10  

#     result = sum_digits(new_number) + last_digit

#     return result

# print(sum_digits(2025))  







# def print_reverse_digits(n):
#     if n == 0:
#         return
#     print(n % 10, end='') 
#     print_reverse_digits(n // 10)  

# print_reverse_digits(2025)  






















# Task 1


# lst = [5, -3, 8, -15, 12, -7, 9, -20, 4, 11]

# print(lst)

# l, r = -1, -1

# for i in range(len(lst)):
#     if lst[i] < 0:
#         if l == -1:
#             l = i
#         r = i

# if l != -1 and r != -1 and l != r:
#     part = lst[l + 1:r]
#     for i in range(len(part)):
#         m = i
#         for j in range(i + 1, len(part)):
#             if part[j] < part[m]:
#                 m = j
#         part[i], part[m] = part[m], part[i]
    
#     lst[l + 1:r] = part

# print(lst)






#Task 2 

# import random

# def shuffle_list(lst):
#     n = len(lst)
#     while n > 1:
#         idx = random.randint(0, n - 1)
#         lst[n - 1], lst[idx] = lst[idx], lst[n - 1]
#         n -= 1
#     return lst


# def find_position(lst, num):
#     return lst.index(num)

# def bubble_sort(lst, reverse=False):
#     n = len(lst)
#     for i in range(n):
#         for j in range(n - 1 - i):
#             if (lst[j] < lst[j + 1] if reverse else lst[j] > lst[j]):
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]

# def custom_sort(lst, pos):
#     left = lst[:pos]
#     right = lst[pos+1:]
#     bubble_sort(left, reverse=True)
#     bubble_sort(right)
#     return left + [lst[pos]] + right

# lst = [3, 15, 7, 1, 20, 9, 12, 18, 5, 6, 17, 2, 8, 4, 13, 16, 10, 14, 11, 19]
# lst = shuffle_list(lst)
# print("Перемішаниц список:", lst)

# rand_num = random.choice(lst)
# pos = find_position(lst, rand_num)
# print(f"Випадкове число: {rand_num}, тайого позиція: {pos}")

# lst = custom_sort(lst, pos)
# print("Оброблений список:", lst)





#11
# try:
#     num1 = float(input("Введіть 1 число: "))
#     num2 = float(input("Введіть 2 число: "))

#     result = num1 / num2

# except ZeroDivisionError:
#     print("Помилка: неможливо поділити на нуль!")
# else:
#     print(result)


# tsk2

#1
# def divide(num1, num2):
#     return num1 / num2

# try:
#     num1 = float(input("Введіть 1 число: "))
#     num2 = float(input("Введіть 2 число: "))

#     result = divide(num1, num2)
#     print(result)

# except ZeroDivisionError:
#     print("Помилка: неможливо поділити на нуль!!")



#2
# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("Помилка: неможливо поділити на нуль!!")

# num1 = float(input("Введіть 1 число: "))
# num2 = float(input("Введіть 2 число: "))

# result = divide(num1, num2)

# print(result)




try:
    usr_input = input("Введіть число: ")

    number = float(usr_input)
    print(number)

except ValueError:
    print("не можна перетворити на число!")







