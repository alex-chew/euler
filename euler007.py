def p(x):
	for d in range(2, int(x**0.5 + 1.5)):
		if not x % d: return False
	return True

c, n = 0, 2
while c < 10001:
	if p(n): c += 1
	n += 1

print(n - 1)

