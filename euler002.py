a, b, sum = 1, 2, 0
while b < 4e+6:
	if not b % 2: sum += b
	a, b = a + 2*b, 2*a + 3*b
print(sum)

