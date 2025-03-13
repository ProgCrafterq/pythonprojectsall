# write/append
# with open("test.txt", "w") as f:
#     f.write("Hello file\n")

# l1= ["one\n","two\n", "three\n"]
#
# with open("test_lines.txt", "w") as f:
#     f.writelines(l1)

# with open("test.txt", "w") as f:
#     print("Some text from print function", file=f)

# read
# with open("test.txt", "r") as f:
#     print(f.read())

# with open("test.txt", "r") as f:
#     #print(f.readlines())
#     for line in f.readlines():
#         print(line, end="")

# with open("test.txt", "r") as f:
#     # while line := f.readline():
#     #     print(line, end="")
#     for line in f:
#         print(line, end="")

# with open("test.txt", "w") as f:
#     print(f.tell())
#     f.write("Hello world")
#     print(f.tell())
#     f.seek(4)
#     print(f.tell())
#     f.write("! Some other text")

# task 1
import re
# with open("test.txt", "r") as f_in:
#     with open("task1.txt", "w") as f_out:
#         for line in f_in:
#             for word in re.split(r"[ ,.:;!?\n()*-+]+",line):
#                 if len(word)>=7:
#                     f_out.write(f"{word}\n")
#
# # with open("test.txt", "r") as f_in, open("task1.txt", "w") as f_out:
# #     f_out.writelines([f"{word}\n" for word in re.split(r"[ ,.:;!?\n()*-+]+",f_in.read()) if len(word)>=7])

# # task 2
# with open("test.txt", "r") as f_in:
#     with open("task2.txt", "w") as f_out:
#         f_out.write(f_in.read())
