import numpy as np


class Neuron:

    def __init__(self, weight_count: int, function):
        self.weight_count = weight_count
        self.function = function
        self.weights = np.random.random_sample(weight_count)

    def get_weight(self, index: int):
        return self.weights[index]

    def work(self, inputs):
        s = 0
        for i in range(self.weight_count):
            s += self.weights[i] * inputs[i]
        return self.function(s)

