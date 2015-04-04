# -*- coding: utf-8 -*-
import math
import operator


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


def get_products(data, i):
    product = lambda x: reduce(operator.mul, x)
    return tuple(map(product, (data[:i], data[i:])))


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
        factorial = reduce(operator.mul, range(target + 1)[1:])
        data = list(devide_primes(factorial, get_primes(target)))

        result = [(1, factorial), (factorial, factorial)]

        devides = (get_products(d, i)
                    for d in get_data_list(data)
                    for i in range(len(d))[1:])
        # devides = ((x, y) for x, y in devides  if x <= y)
        result += sorted(set((i, factorial) for x in devides
                                            for i in x))

        tmp = []
        prime_freq = [(prime, len(filter(lambda i: i == prime, data))) for prime in set(data)]
        for p, f in prime_freq:
            left = math.pow(p, f)
            right = (math.pow(*pf) for pf in prime_freq if pf != (p, f))
            right = reduce(operator.mul, right)
            for r in (math.pow(p, i) * right for i in range(f)):
                tmp.append(tuple(sorted([left, r])))
        result += set(tmp)

        return result

if __name__ == '__main__':
    result = get_common_multiple(6)
    if result:
        print len(result)
        for x, y in result:
            print (x, y)
