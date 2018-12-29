import random


class Neuron:

    def __init__(self, weight_count: int, function, derived_function):
        self.weight_count = weight_count
        self.function = function
        self.derived_function = derived_function
        self.weights = [random.uniform(0.0, 1.0) for i in range(weight_count)]
        self.bias = random.uniform(0.0, 1.0)
        self.recent_value = 0
        self.derived_value = 0
        self.error = 0

    def work(self, inputs: []):
        s = 0
        for i in range(self.weight_count):
            s += self.weights[i] * inputs[i]
        s += self.bias
        self.recent_value = self.function(s)
        self.derived_value = self.derived_function(s)
        return self.recent_value
