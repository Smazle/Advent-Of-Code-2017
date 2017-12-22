import numpy as np

inp = 312051
#inp = 52

sqrt = np.ceil(np.sqrt(inp))
ring = sqrt if sqrt % 2 == 1 else sqrt + 1


idx = inp - (ring-2)**2

iteration = (idx/ring-1)/2

for i in range(iteration):
    





(X,Y) = (ring-2, ring-2)






