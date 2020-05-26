import math

squares = 0
for i in range(1,101):
	j = i ** 2
	squares = squares + j

sumSquares = 0
for i in range(1,101):
	sumSquares = sumSquares + i

sumSquares = sumSquares ** 2

difference = sumSquares - squares
print(difference)