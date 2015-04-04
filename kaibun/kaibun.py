
def is_kaibun(text):
    length = len(text)
    predict = lambda i: text[i] == text[length - 1 - i] 
    return all(predict(i) for i in range(length / 2))

print is_kaibun("abcdcba")
print is_kaibun("abccba")
print is_kaibun("abecba")

def kaibun(text):
    return text == "".join(reversed(text))

print kaibun("abccba")
