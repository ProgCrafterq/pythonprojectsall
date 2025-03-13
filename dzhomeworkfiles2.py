#task1
try:
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        l1, l2 = f1.readlines(), f2.readlines()

    if len(l1) != len(l2):
        print("Diff len")

    length = len(l1)
    if len(l2) < len(l1):  
        length = len(l2)  

    for i in range(length):
        if l1[i].strip() != l2[i].strip():
            print(f"Line {i+1}:\nfile1: {l1[i]}file2: {l2[i]}")

    if len(l1) > len(l2):
        print(f"Extra in file1 from line {len(l2)+1}:")
        for i in range(len(l2), len(l1)):  
            print(l1[i], end="")

    elif len(l2) > len(l1):
        print(f"Extra in file2 from line {len(l1)+1}:")
        for i in range(len(l1), len(l2)): 
            print(l2[i], end="")
            
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)


# task 2
try:
    v = "aeiouаеєиіїоуюяAEIOUАЕЄИІЇОУЮЯ"
    c = "bcdfghjklmnpqrstvwxyzбвгґджзйклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXYZБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ"

    with open("data.txt", "r") as d:
        t = d.read()
        ch = 0
        ln = 0
        v_count = 0
        c_count = 0
        d_count = 0

        for sym in t:
            ch += 1
            if sym in v:
                v_count += 1
            elif sym in c:
                c_count += 1
            elif sym.isdigit():
                d_count += 1

        ln = t.count('\n') + 1

    with open("statistics.txt", "w") as s:
        s.write(f"Characters = {ch}\nLines = {ln}\nVowels = {v_count}\nConsonants = {c_count}\nDigits = {d_count}")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

# task 3
try:
    with open("data.txt", "r") as d:
        lines = []
        for line in d:
            lines.append(line)

    with open("new_data.txt", "w") as n:
        for i in range(len(lines) - 1):
            n.write(lines[i])
except FileNotFoundError as e:
    print(e)

# task 4
try:
    max_len = 0
    with open("data.txt", "r") as d:
        for line in d:
            length = 0
            for _ in line:
                length += 1
            if length > max_len:
                max_len = length

    print(f"Max len = {max_len}")
except FileNotFoundError as e:
    print(e)

# task 5
try:
    w = input("Word? ")
    count = 0
    with open("data.txt", "r") as d:
        for line in d:
            pos = 0
            while True:
                pos = line.find(w, pos)
                if pos == -1:
                    break
                count += 1
                pos += len(w)

    print(f"{w} = {count}")
except FileNotFoundError as e:
    print(e)

# task 6
try:
    old_w = input("Replace? ")
    new_w = input("With? ")

    with open("data.txt", "r") as d:
        text = ""
        for line in d:
            while old_w in line:
                line = line.replace(old_w, new_w, 1)
            text += line

    with open("new_data.txt", "w") as n:
        n.write(text)
except FileNotFoundError as e:
    print(e)
