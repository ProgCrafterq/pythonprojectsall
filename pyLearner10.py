# import random

# list1 = []
# list2 = []

# for _ in range(10):
#     list1.append(random.randint(1, 100))
#     list2.append(random.randint(1, 100))

# print("Список 1:", list1)
# print("Список 2:", list2)

# combined_list = []
# for item in list1:
#     combined_list.append(item)
# for item in list2:
#     combined_list.append(item)
# print("\n1. Об'єднаний список:", combined_list)

# unique_combined_list = []
# for item in combined_list:
#     if item not in unique_combined_list:
#         unique_combined_list.append(item)
# print("2. Об'єднаний список без повторів:", unique_combined_list)

# common_elements = []
# for item in list1:
#     if item in list2 and item not in common_elements:
#         common_elements.append(item)
# print("3. Спільні елементи:", common_elements)

# unique_elements = []
# for item in list1:
#     if item not in list2 and item not in unique_elements:
#         unique_elements.append(item)
# for item in list2:
#     if item not in list1 and item not in unique_elements:
#         unique_elements.append(item)
# print("4. Унікальні елементи кожного зі списків:", unique_elements)

# min1 = list1[0]
# max1 = list1[0]
# min2 = list2[0]
# max2 = list2[0]

# for item in list1:
#     if item < min1:
#         min1 = item
#     if item > max1:
#         max1 = item

# for item in list2:
#     if item < min2:
#         min2 = item
#     if item > max2:
#         max2 = item

# min_max_values = [min1, max1, min2, max2]
# print("5. Мінімальні та максимальні значення:", min_max_values)






# def display_text():
#     print("\033[90mDon't let the noise of others' opinions\ndrown out your own inner voice.\033[0m")
#     print("\033[93mSteve Jobs\033[0m")

# display_text()



# def display_neparn_numbers():
#     start = int(input("Введіть 1: "))
#     end = int(input("Введіть 2: "))
    
#     for num in range(start, end):
#         if num % 2 != 0:
#             print(num)

# display_neparn_numbers()


# def display_neparn_numbers(start, end):
#     for num in range(start, end):
#         if num % 2 != 0:
#             print(num)

# display_neparn_numbers(5, 15)


# def draw_line(length, direction, symbol):
#     if direction == "h":
#         for q in range(length):
#             print(symbol, end="")
#         print()  

#     elif direction == "v":
#         for i in range(length):
#             print(symbol)
#     else:
#         print("err")

# length = int(input("Введіть довжину лінії: "))
# direction = input("Введіть напрямок 'h' або 'v': ")
# symbol = input("Введіть символ: ")

# draw_line(length, direction, symbol)




def find_max(a, b, c, d):
    if a >= b and a >= c and a >= d:
        return a
    elif b >= a and b >= c and b >= d:
        return b
    elif c >= a and c >= b and c >= d:
        return c
    else:
        return d

num1 = int(input("Введіть 1 число: "))
num2 = int(input("Введіть 2 число: "))
num3 = int(input("Введіть 3 число: "))
num4 = int(input("Введіть 4 число: "))

max_num = find_max(num1, num2, num3, num4)
print("Максимальне число:", max_num)




