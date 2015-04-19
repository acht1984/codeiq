# -*- coding: utf-8 -*-
import math
import operator
import itertools


def get_primes(stop):
    yield 2
    start = 3
    for i in xrange(start, stop + 1, 2):
        if all(i % j for j in xrange(start, int(math.sqrt(i)) + 1, 2)):
            yield i


def devide_primes(num, primes):
    for prime in primes:
        while num % prime == 0:
            yield prime
            num /= prime


def product(x):
    return reduce(operator.mul, x, 1)


def common_devide(x, y):
    return product(i for i in x for j in y if i == j)


def common_multiple(x, y):
    return x[0] * y[0] / common_devide(set(x[1]), set(y[1]))


def get_data_list(data):
    for i in range(len(data)):
        n = list(data)
        for j in range(i):
            datum = n.pop(0)
            n.append(datum)
        yield n


def get_common_multiple(target):
    if target < 1:
        return None
    if target == 1:
        return [(target, target)]
    if target == 2:
        return [(1, target), (target, target)]
    else:
        factorial = product(range(target + 1)[1:])
        primes = list(get_primes(target))
        data = list(devide_primes(factorial, primes))

        result = [(1, factorial), (factorial, factorial)]

        devides = set((product(d[:i]), tuple(sorted(d[:i])))
                      for d in get_data_list(data)
                      for i in range(len(d))[1:])
        result += sorted(set((x, factorial) for x, items in devides))

        products = ((x[0], y[0])
                    for x, y in itertools.permutations(devides, 2)
                    if x[0] <= y[0]
                    if y[0] % x[0] != 0
                    if common_multiple(x, y) == factorial)
        result += list((x, y) for x, y in products)

        return result

if __name__ == '__main__':
    result = get_common_multiple(6)
    if result:
        print len(result)
        # for x, y in result:
        #     print (x, y)
