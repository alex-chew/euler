def pf(x):
	f, i = [], 2
	while i <= x:
		if not x%i:
			x /= i
			f.append(i)
		else: i += 1
	return f

def lcm(l):
	pd = {}
	for n in l:
		fs = pf(n)
		d = dict((f, fs.count(f)) for f in set(fs))
		for x, c in d.iteritems():
			pd[x] = max(pd[x], c) if x in pd.keys() else c
	p = 1
	for x, c in pd.iteritems(): p *= x**c
	return p

print(lcm(range(1, 20)))

