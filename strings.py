# import math
# start = int(input("Enter the start->"))
# finish = int(input("Enter the finish->"))
#
# if start > finish:
#     start, finish = finish, start
#
# for num in range(start, finish):
#     prime = True
#     for i in range(2, int(math.sqrt(num)+1)):
#         if num % i == 0:
#             prime = False
#             break
#     if prime and num != 1:
#         print(num, end=" ")


# line = "Hello"

# for i in range(len(line)):
#     print(line[i])

# for ch in line:
#     print(ch)

# print("Hello".count("l"))

# print("Hello".upper())
# print("Helloß".lower())
# print("Helloß".casefold())
# print("Hello World".capitalize())
# print("Hello world".title())
# print("Hello".swapcase())
#
# print("Hello".index("l"))
# print("Hello".rindex("l"))
# print("Hello".find("l"))
# print("Hello".rfind("l"))


# print("Hello".startswith("He"))
# print("Hello".endswith("o"))

# print("Hello".ljust(10,"_"))
# print("Hello".rjust(10,"0"))
# print("Hello".center(10))
# print("Hello".zfill(10))

# print("   Hello   ".strip())
# print("   Hello   ".lstrip())
# print("   Hello   ".rstrip())


# print("Hello".isidentifier())
# print("Hello".replace("l", "L"))

# words = "one two three four five".split()
# print(words)
#
# line = ", ".join(words)
# print(line)

# # Today is 12 December 2024!
# day = 12
# month = "December"
# year = 2024
# # today = "Today is "+str(day)+" "+month+" "+str(year)+"!"
# # today = "Today is {0} {1} {2}!".format(day, month, year)
# today = f"Today is {day} {month} {year}!"
# # today = "Today is %d %s %d!" % (day, month, year)
# print(today)

# line = "Hello world"

# print(line[0:7])
# print(line[-1:-6:-1])


# # task 1
# line = input("Enter some text->")
#
# line = line[::-1]
# print(line)


# # task 2
# line = input("Enter some text->")
#
# digits = 0
# letters = 0
#
# for symbol in line:
#     if symbol.isdigit():
#         digits += 1
#     if symbol.isalpha():
#         letters += 1
# print(f"Length = {len(line)}, Digits = {digits}, Letters = {letters}")




# words = input("enter words separated by space ->").split()
