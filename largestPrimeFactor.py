num = 12345
factors = []
primes = []
nonPrimes = []


def diff(factors, nonPrimes):
    return list(set(factors) - set(nonPrimes))


for i in range(2, num):
    if num % i == 0:
        factors.append(i)

for factor in factors:
    for j in range(2, factor):
        if factor % j == 0:
            nonPrimes.append(factor)
nonPrimes = list(dict.fromkeys(nonPrimes))
primes = diff(factors, nonPrimes)
primes.sort()
print(primes[-1])
