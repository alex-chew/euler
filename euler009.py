for m in range(40):
	for n in range(40):
		a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
		if a + b + c == 1000:
			print(a * b * c)
			exit()

