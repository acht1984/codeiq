# -*- coding: utf-8 -*-

with open("./words.txt") as f:
    source = [num[:-1] for num in f]
    nums = source[:20]
    tens = ["", ""] + source[20:28]
    hundred = source[28]
    thousands = [""] + source[29:32]
    negative = source[32]


def devide(digit):
    result = [(n, []) for n in thousands]
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


def isZero(digit):
    return len(digit) == 1 and digit == "0"


def extractSign(digit):
    if digit and digit[0] == "-":
        return digit[1:], negative + " "
    else:
        return digit, ""


def toEnglish(num):
    if isZero(num):
        return nums[0]
    num, text = extractSign(num)
    text += " ".join(" ".join(values + [key]).rstrip()
                     for key, values in reversed(devide(num))
                     if not all("" == v for v in values))
    return text

for num in open("./testdata.in.txt"):
    print toEnglish(num[:-1])
