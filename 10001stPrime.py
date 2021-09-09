products = []
primes = []
nonPrimes = []

def diff(products, nonPrimes):
    return list(set(products) - set(nonPrimes))

for i in range(2, 100001):
	for j in range(2, 100001):
		products.append(i)
		if i % j == 0 and j != i:
			nonPrimes.append(i)

nonPrimes = list(dict.fromkeys(nonPrimes))
primes = diff(products, nonPrimes)
nonPrimes.sort()
print(primes[10000])