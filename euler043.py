from itertools import permutations

lt = [(2, 2), (3, 3), (4, 5), (5, 7), (6, 11), (7, 13), (8, 17)]
pn = []
for p in permutations(range(10)):
	for (s, d) in lt:
		n = 100*p[s-1] + 10*p[s] + p[s+1]
		if n % d != 0: break
	else: pn.append(int(''.join([str(i) for i in p])))

print(sum(pn))

