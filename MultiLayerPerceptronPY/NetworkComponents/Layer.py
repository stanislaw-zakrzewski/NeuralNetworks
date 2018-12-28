from NetworkComponents.Neuron import Neuron


class Layer:

    def __init__(self, weights_count: int, neurons_count: int, function):
        self.neuron_count = neurons_count
        self.neurons = [Neuron(weights_count, function) for i in range(neurons_count)]

    def work(self, inputs):
        ret = []
        for i in range(self.neuron_count):
            ret.append(self.neurons[i].work(inputs))
        return ret
