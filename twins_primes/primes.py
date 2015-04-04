def primes(num):
    result = []
    targets = range(2, num + 1)
    while len(targets):
        prime = targets[0]
        result.append(prime)
        targets = filter(lambda x: x % prime, targets)
    return result

first = (f for f in primes(1000))
second = (s for s in primes(1000)[1:] + [0])
twins = ((f, s) for f, s in zip(first, second) if s - f == 2)
print ", ".join(str(pair) for pair in twins)
