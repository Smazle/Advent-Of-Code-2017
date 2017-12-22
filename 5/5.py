import numpy as np


inp = np.loadtxt("./input", dtype=int, delimiter="\n")

idx = 0
steps = 0

while len(inp) > idx >= 0:
    try:
        inp[idx] += 1

        if inp[idx]-1 != 0:
            steps += 1

        idx += inp[idx]-1
    except:
        break
        

print steps
