m = 0
for i in range(999, 1, -1):
	for j in range(999, 1, -1):
		p = str(i*j)
		if p[::-1] == p: m = max(m, i*j)
print(m)

