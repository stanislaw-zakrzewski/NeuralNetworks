import numpy as np


def linear_function(x):
    return a * x + b


a = 1
b = 0
examples_count = 100
file = open("input.txt", "a")

file.seek(0)
file.truncate()

for i in range(examples_count):
    x = np.random.rand(1)[0] * 10
    y = np.random.rand(1)[0] * 10
    d = 1 if linear_function(x) > y else 0
    print(str(x) + ' ' + str(y) + ' ' + str(d))
    file.write(str(x) + ' ' + str(y) + ' ' + str(d) + '\n')
