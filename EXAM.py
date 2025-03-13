# Task 1
# def task1_show_substring():
#     try:
#         s = input("Введіть рядок: ")
#         try:
#             m = int(input("Введіть позицію m:"))
#             n = int(input("Введіть позицію n:"))
#         except Exception as e:
#             print("Exception:", e)
#             return
#         result = ""
#         i = m - 1  
#         while i < n and i < len(s):
#             result += s[i]
#             i += 1
#         print("Результат (символи з m по n):", result)
#     except Exception as e:
#         print(e)

# task1_show_substring()


#-----------------------------------------------------------------------------------------------


# # Task 2
# def task2_delete_substring():
#     try:
#         s = input("Введіть рядок: ")
#         try:
#             m = int(input("Введіть позицію m: "))
#             n = int(input("Введіть позицію n: "))
#         except Exception as e:
#             print("Exception:", e)
#             return
#         result = ""
#         i = 0
#         while i < len(s):
#             if i < m - 1 or i >= n:
#                 result += s[i]
#             i += 1
#         print("Результат (рядок m до n):", result)
#     except Exception as e:
#         print( e)

# task2_delete_substring()


#-----------------------------------------------------------------------------------------------




# Task 3
# def task3_all_positions():
#     try:
#         s = input("Введіть рядок: ")
#         ch = input("Введіть символ для пошуку: ")
#         positions = []
#         pos = 1
#         for char in s:
#             if char == ch:
#                 positions.append(pos)
#             pos += 1
#         if positions:
#             print(f"Позиції символу '{ch}':", positions)
#         else:
#             print(f"Символ '{ch}' не знайдено у рядку.")
#     except Exception as e:
#         print(е)

# task3_all_positions()




#-----------------------------------------------------------------------------------------------



# Task 4
# def task4_last_position():
#     try:
#         s = input("Введіть рядок: ")
#         ch = input("Введіть символ для пошуку: ")
#         last_pos = 0
#         pos = 1
#         for char in s:
#             if char == ch:
#                 last_pos = pos
#             pos += 1
#         if last_pos != 0:
#             print(f"Остання позиція символу '{ch}':", last_pos)
#         else:
#             print(f"Символ '{ch}' не знайдено у рядку.")
#     except Exception as e:
#         print(е)

# task4_last_position()

#-----------------------------------------------------------------------------------------------


#Task5


# import random

# def task5_lists():
#     try:
#         list_I = []
#         list_II = []
#         list_III = []
#         i = 0
#         while i < 10:
#             num = random.randint(-12, 12)
#             list_I.append(num)
#             if num % 2 == 0:
#                 list_II.append(True)
#             else:
#                 list_II.append(False)
#             if num < 0:
#                 list_III.append(-1)
#             elif num > 0:
#                 list_III.append(1)
#             else:
#                 list_III.append(0)
#             i += 1
#         print("Список I:", list_I)
#         print("Список II (парність):", list_II)
#         print("Список III (заміна значень):", list_III)
#     except Exception as e:
#         print(е)

# task5_lists()



#-----------------------------------------------------------------------------------------------




# # Task 6
# def print_list(lst):
#     try:
#         i = 0
#         while i < len(lst):
#             print(lst[i], end=" ")
#             i += 1
#         print()
#     except Exception as e:
#         print(e)

# data = input("Введіть елементи списку через пробіл: ").split()
# print_list(data)



#-----------------------------------------------------------------------------------------------



# Task 7



# def is_even(list_numbers):
#     try:
#         count_even = 0  
#         count_odd = 0   
#         i = 0
        
#         while i < len(list_numbers):
#             if list_numbers[i] % 2 == 0:
#                 count_even += 1  
#             else:
#                 count_odd += 1   
#             i += 1
        
#         if count_even > count_odd:
#             print("парний список")  
#         elif count_odd > count_even:
#             print("непарний список")  
#         else:
#             print("Кількість парних та непарних чисел рівні")  
#     except Exception as e:
#         print(е)

# data = input("Введіть числа через пробіл: ").split()
# numbers = [int(x) for x in data]  
# is_even(numbers)




#-----------------------------------------------------------------------------------------------



# # Task 8


# def bubble_sort_asc(lst):
#     try:
#         n = len(lst)
#         sorted_list = lst[:]
#         i = 0
#         while i < n:
#             j = 0
#             while j < n - i - 1:
#                 if sorted_list[j] > sorted_list[j+1]:
#                     temp = sorted_list[j]
#                     sorted_list[j] = sorted_list[j+1]
#                     sorted_list[j+1] = temp
#                 j += 1
#             i += 1
#         return sorted_list
#     except Exception as e:
#         print(e)
#         return lst

# def bubble_sort_desc(lst):
#     try:
#         n = len(lst)
#         sorted_list = lst[:]
#         i = 0
#         while i < n:
#             j = 0
#             while j < n - i - 1:
#                 if sorted_list[j] < sorted_list[j+1]:
#                     temp = sorted_list[j]
#                     sorted_list[j] = sorted_list[j+1]
#                     sorted_list[j+1] = temp
#                 j += 1
#             i += 1
#         return sorted_list
#     except Exception as e:
#         print(e)
#         return lst

# def sort_list(lst, number):
#     try:
#         pos = -1
#         i = 0
#         while i < len(lst):
#             if lst[i] == number:
#                 pos = i
#                 break
#             i += 1
#         if pos == -1:
#             raise ValueError("Число не знайдено тут")
#         left_part = []
#         i = 0
#         while i < pos:
#             left_part.append(lst[i])
#             i += 1
#         right_part = []
#         i = pos + 1
#         while i < len(lst):
#             right_part.append(lst[i])
#             i += 1
#         left_sorted = bubble_sort_asc(left_part)
#         right_sorted = bubble_sort_desc(right_part)
#         new_list = []
#         i = 0
#         while i < len(left_sorted):
#             new_list.append(left_sorted[i])
#             i += 1
#         new_list.append(lst[pos])
#         i = 0
#         while i < len(right_sorted):
#             new_list.append(right_sorted[i])
#             i += 1
#         print("Результат сортування:", new_list)
#     except Exception as e:
#         print(e)

# data = input("Введіть елементи списку пробілamu: ").split()
# lst = []
# i = 0
# while i < len(data):
#     try:
#         lst.append(int(data[i]))
#     except:
#         lst.append(0)
#     i += 1
# try:
#     num = int(input("Введіть число: "))
# except Exception as e:
#     print("Exception:", e)
#     num = 0
# sort_list(lst, num)



#-----------------------------------------------------------------------------------------------

# # Task 9
# def graph(list_I):



#     try:
#         i = 0
#         while i < len(list_I):
#             num = list_I[i]
#             bar = ""
#             if num >= 0:
#                 j = 0
#                 while j < num:
#                     bar += "*"
#                     j += 1
#             else:
#                 j = 0
#                 while j < -num:
#                     bar += "*"
#                     j += 1
#                 bar = "-" + bar
#             print(bar)
#             i += 1
#     except Exception as e:
#         print("Виникла помилка у Task 9:", e)


#-----------------------------------------------------------------------------------------------

# # Task 10
def square(list_I):
    try:
        i = 0
        while i < len(list_I):
            num = list_I[i]
            if num > 0:
                print(num)
                j = 0
                while j < num:
                    line = ""
                    k = 0
                    while k < num:
                        line += "#"
                        k += 1
                    print(line)
                    j += 1
                print()
            i += 1
    except Exception as e:
        print(e)


        
