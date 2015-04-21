# -*- coding: utf-8 -*-

with open("./words.txt") as f:
    source = [num[:-1] for num in f]
    nums = source[:20]
    tens = source[20:28]
    bigs = source[28:32]
    negative = source[32]

print tens
print bigs
print negative
