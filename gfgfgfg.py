# Task1
# with open("output.txt", "w") as f:
#     f.write("Hello, world!")

#Task2
# with open("output.txt", "r") as f:
#     print(f.read())
#Task3
# with open("data.txt", "r") as f_in:
#     with open("backup.txt", "w") as f_out:
#         f_out.write(f_in.read())
#Task4
# with open("data.txt", "r") as f:
#     line_count = 0
#     for line in f:
#         line_count += 1
#     print(line_count)
#Task5
# with open("data.txt", "r") as f:
#     line_count = 0
#     word_count = 0
#     char_count = 0
#     for line in f:
#         line_count += 1
#         word_count += len(line.split())
#         char_count += len(line)

# with open("summary.txt", "w") as f_out:
#     f_out.write(f"{line_count}\n")
#     f_out.write(f"{word_count}\n")
#     f_out.write(f"{char_count}\n")
#     #Task1
# with open("numbers.txt", "r") as f:
#     numbers = f.readlines()

# total_all = 0
# for num in numbers:
#     total_all += int(num)

# with open("sum.txt", "w") as f_out:
#     f_out.write(str(total_all))
#tsk2
# file_namee = input()
# word = input()

# with open(file_namee, "r") as f:
#     content = f.read()

# def count_word(text, target):
#     count = 0
#     words = text.split()  
#     for w in words:
#         if w == target:
#             count += 1
#     return count

# result = count_word(content, word)

# print(result)
#tsk3
with open("merged.txt", "w") as f_out:
    for f_name in ["file1.txt", "file2.txt", "file3.txt"]:
        f_out.write(f"==== {f_name} ====\n")  
        with open(f_name, "r") as f_in:
            f_out.write(f_in.read())  
            f_out.write("\n")  










