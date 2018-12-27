import numpy as np


class Neuron:
    def __init__(self, weights_count):
        self.weights = np.random.rand(weights_count)

    def get_weights(self):
        return self.weights

    def update_weight(self, weight_number, value_to_add):
        self.weights[weight_number] += value_to_add
