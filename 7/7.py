import numpy as np


weights = {}
relations = {}


main = "gmcrj"


with open("./input") as f:
    for line in f:
        line = line.rstrip()
        line = line.replace(",", "")
        line = line.split(" ") 

        name = line[0]
        weights[name] = int(line[1].strip("()"))

        if len(line) > 2:
            relations[name] = line[3:]
        else:
            relations[name] = []


