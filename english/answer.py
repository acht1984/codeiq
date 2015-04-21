# -*- coding: utf-8 -*-

with open("./words.txt") as f:
    source = [num[:-1] for num in f]
    nums = source[:20]
    tens = source[20:28]
    hundred = source[28]
    bigs = source[29:32]
    negative = source[32]


def toEnglish(digit):
    length = len(digit)
    if length == 1 and digit == "0":
        return nums[0]

print toEnglish("0")
