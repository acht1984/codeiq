def sum_nums(num):
    result = 0
    while num > 0:
        result += num % 10
        num /= 10
    return result

def primes(num):
    result = [1, 2]
    for i in map(lambda x: x + 1, range(num)):
        for prime in result[1:]:
            while i % prime == 0:
                i /= prime
            if i not in result:
                result.append(i)
    return result[1:]

def devide_primes(num, primes):
    result = []
    for prime in primes:
        while num % prime == 0: 
            result.append(prime)
            num /= prime
    return result


if __name__ == '__main__':
    target = 10000
    primes = primes(target / 2)
    for num in map(lambda x: x + 1, range(target)):
        wa = sum_nums(num)
        soinsu = devide_primes(num, primes)
        if wa == len(soinsu) - 1:
            print num, wa, soinsu

