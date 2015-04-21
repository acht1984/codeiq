# -*- coding: utf-8 -*-

with open("./words.txt") as f:
    source = [num[:-1] for num in f]
    nums = source[:20]
    tens = source[20:28]
    hundred = source[28]
    bigs = source[29:32]
    negative = source[32]

print tens
print hundred
print bigs
print negative
