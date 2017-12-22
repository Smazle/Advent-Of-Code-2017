import numpy as np
from itertools import permutations

data = [x.replace("\n", "").split(" ") for x in open("./input", "r").readlines()]

print len([x for x in data if len(x) == len(set(x))])

print len([x for x in data if len(x) == len(set(map(lambda n: "".join(sorted(n)), x)))])
