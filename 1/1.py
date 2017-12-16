import numpy as np

data = [int(x) for x in list(open("input", "r").read())[:-1]]

print sum([x for idx, x in enumerate(data) 
    if idx != len(data) and data[idx-1] == x])

print sum([x for idx, x in enumerate(data) 
    if idx != len(data) and data[idx-len(data)/2] == x])
