#task 3
# try:
#     with open("data.txt", "r") as data:
#         with open("backup.txt", "w") as backup:
#             backup.write(data.read())
# except FileNotFoundError as ex:
#     print(ex)



# #task 5
# import re
# try:
#     with open("data.txt", "r") as data:
#         text = data.read()
#         lines = len(text.split("\n"))
#         words = len(re.split(r"[- ,.:;!?\n\t]+", text))
#         characters = len(text)
#     with open("summary.txt", "w") as summary:
#         summary.write(f"Lines = {lines}\n"
#                       f"words = {words}\n"
#                       f"characters = {characters}")
# except FileNotFoundError as ex:
#     print(ex)


# # task 6
#
# def shift_symbol(c:str)->str:
#     if len(c) > 1:
#         raise  ValueError(f"str {c} must have one symbol")
#     letters = "abcdefghijklmnopqrstuvwxyz"
#     if c in letters:
#         return letters[(letters.index(c)+1)%26]
#     if c in letters.upper():
#         return letters.upper()[(letters.upper().index(c)+1)%26]
#     return c
#
# try:
#     with open("data.txt", "r") as data:
#         text = data.read()
#     with open("encrypted.txt", "w") as encrypted:
#         encrypted.write("".join([shift_symbol(c) for c in text]))
# except Exception as ex:
#     print(ex)


#task 2.1

try:
    s = 0
    with open("numbers.txt", "r") as numbers:
        for num in numbers.read().split():
            s+=int(num)
    with open("sum.txt", "w") as f_sum:
        f_sum.write(str(s))
except Exception as ex:
    print(ex)