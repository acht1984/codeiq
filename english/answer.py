# -*- coding: utf-8 -*-

# 数字->英語変換表の作成
with open("./words.txt") as f:
    source = [digit[:-1] for digit in f]
    nums = source[:20]
    tens = ["", ""] + source[20:28]
    hundred = source[28]
    thousands = [""] + source[29:32]
    negative = source[32]


def isZero(digit):
    return len(digit) == 1 and digit == "0"


def devideSign(digit):
    if digit and digit[0] == "-":
        return digit[1:], negative + " "
    else:
        return digit, ""


def extract(digit, i):
    return [n for j, n in enumerate(reversed(digit)) if j/3 == i]


def to_num(num):
    if num[0] == "0":
        return ""
    return nums[int(num[0])]


def to_ten(num):
    n, t = num
    if t == "0":
        return to_num(n)
    elif t == "1":
        return nums[int(t + n)]
    elif n == "0":
        return tens[int(t)]
    else:
        return "{0} {1}".format(tens[int(t)], nums[int(n)])


def to_hundred(num):
    n, t, h = num
    if h == "0":
        return to_ten(n+t)
    else:
        return "{0} {1} {2}".format(nums[int(h)], hundred, to_ten(n+t))


def convert(num):
    if len(num) == 0:
        return ""
    elif len(num) == 1:
        return to_num(num)
    elif len(num) == 2:
        return to_ten(num)
    else:
        return to_hundred(num)


def toEnglish(digit):
    if isZero(digit):
        return nums[0]
    # マイナス符号を先に処理
    digit, text = devideSign(digit)
    # 千の表記ごとに(数値表記, 千の表記)のペアを作成
    converted = [
        (convert(extract(digit, i)), x) for i, x in enumerate(thousands)]
    # 数値表記がないものを除外 ex.000
    filtered = ((n, x) for n, x in reversed(converted) if n)
    return text + " ".join(" ".join(x) for x in filtered)[:-1]


if __name__ == '__main__':
    for digit in open("./testdata.in.txt"):
        print toEnglish(digit[:-1])
