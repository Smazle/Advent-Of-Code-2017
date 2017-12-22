import numpy as np

data = np.loadtxt("./input", dtype=np.int)

print sum([max(x) - min(x) for x in data])

print np.array([[b/q for b in x for q in x if b%q == 0 and q != b] for x in data]).sum()
