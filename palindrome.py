products = []
palindromeProducts = []
for i in range(2, 1000):
	for j in range(2, 1000):
		k = i * j
		products.append(k)
list(set(products))

for product in products:
	product = str(product)
	if product == product[::-1]:
		product = int(product)
		palindromeProducts.append(product)
palindromeProducts.sort()
print(palindromeProducts)
