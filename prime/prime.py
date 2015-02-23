#!/usr/bin/env python
#encoding: utf-8
from math import log, ceil

def sum_nums(num):
    result = 0
    while num > 0:
        result += num % 10
        num /= 10
    return result

def primes(num):
    result = []
    targets = range(2, num + 1)
    while len(targets):
        prime = targets[0]
        result.append(prime)
        targets = filter(lambda x: x % prime, targets)
    return result

def devide_primes(num, primes, wa):
    result = []
    for prime in primes:
        while num % prime == 0: 
            result.append(prime)
            num /= prime
        if num == 1:
            return result
    return result


if __name__ == '__main__':
    target = 10000
    # 解には少なくとも一つの積があり、その最小値は2
    # そのため素数リストの終端値を予め1/2する
    primes = primes(target / 2)
    # かけるの数も2の倍数の時が最大
    limit = int(log(target, 2))
    for num in range(1000, target):
        wa = sum_nums(num)
        if wa > limit:
            continue
        soinsu = devide_primes(num, primes, wa)
        if wa == len(soinsu) - 1:
            print num, wa, soinsu

