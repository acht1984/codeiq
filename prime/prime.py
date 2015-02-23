#!/usr/bin/env python
#encoding: utf-8

def sum_nums(num):
    result = 0
    while num > 0:
        result += num % 10
        num /= 10
    return result

def primes(num):
    result = [2]
    # 2以外の素数はすべて奇数
    for i in range(3, num + 1, 2):
        # それまでの素数で割れなければiは素数
        if reduce(lambda x, y: x and i % y != 0, result, True):
            result.append(i)
    return result

def devide_primes(num, primes):
    result = []
    for prime in primes:
        while num % prime == 0: 
            result.append(prime)
            num /= prime
    return result


if __name__ == '__main__':
    target = 10000
    # 解には少なくとも一つの積があり、その最小値は2
    # そのため素数リストの終端値を予め1/2する
    primes = primes(target / 2)
    for num in range(1000, target):
        wa = sum_nums(num)
        soinsu = devide_primes(num, primes)
        if wa == len(soinsu) - 1:
            print num, wa, soinsu

