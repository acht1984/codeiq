# -*- coding: utf-8 -*-

with open("./words.txt") as f:
    source = [num[:-1] for num in f]
    nums = source[:20]
    tens = ["", ""] + source[20:28]
    hundred = source[28]
    bigs = [""] + source[29:32]
    negative = source[32]


def devide(digit):
    result = [(n, []) for n in bigs]
    length = len(digit)
    if length == 1 and digit == "0":
        key, data = result[0]
        data.append(nums[0])
        return result
    first = ""
    for i, n in enumerate(reversed(digit)):
        key, data = result[i/3]
        if i % 3 == 0:
            first = n
            data.append(nums[int(n)])
            continue
        if i % 3 == 1:
            del data[0]
            if n in ("0", "1"):
                data.append(nums[int(n + first)])
            elif first == "0":
                data.append(tens[int(n)])
            else:
                data.append(tens[int(n)])
                data.append(nums[int(first)])
        if i % 3 == 2:
            if n != "0":
                data.insert(0, hundred)
                data.insert(0, nums[int(n)])
    return result


def toEnglish(num):
    text = ""
    if num and num[0] == "-":
        text = negative + " "
        num = num[1:]
    text += " ".join(" ".join(values + [key])
                     for key, values in reversed(devide(num))
                     if "".join(values))
    return text

for num in open("./testdata.in.txt"):
    print toEnglish(num[:-1])
