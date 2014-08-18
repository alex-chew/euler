def p(x):
	for d in range(2, int(x**0.5 + 1.5)):
		if not x % d: return False
	return True

print(sum([n for n in range(2, 2000000) if p(n)]))

