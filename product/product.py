# coding=utf_8
import math

# 指定の数までの素数リストを返す
def primes(stop):
    if stop < 2:
        yield None
    else:
        yield 2
        for i in range(3, stop + 1, 2):
            if all(i % j for j in range(3, int(math.sqrt(i)) + 1, 2)):
                yield i


stop = 1000
prime_list = list(primes(stop))

is_not_prime = lambda x: x not in prime_list

min_prime = lambda x: next(prime for prime in prime_list if x % prime == 0)

# 長方形の合成数
products = ((i, min_prime(i), i / min_prime(i))
            for i in xrange(2, stop + 1) if is_not_prime(i))
# 直方体の合成数
products = ((i, j, min_prime(k), k / min_prime(k))
            for i, j, k in products if is_not_prime(k))

# 合瀬数を抽出
products = list(products)

print len(products)
for i in products:
    print i
