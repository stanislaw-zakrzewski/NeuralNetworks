import random
from functions import f_identity, fp_identity, f_sigmoid, fp_sigmoid


class Network:

    def __init__(self, input_count: int, output_count: int, hidden_layers_count: int,
                 neurons_on_hidden_layer_count: int):
        self.layers = []
        if hidden_layers_count > 0:
            self.layers.append(Layer(input_count, neurons_on_hidden_layer_count, f_sigmoid, fp_sigmoid))
        for i in range(hidden_layers_count - 1):
            self.layers.append(
                Layer(neurons_on_hidden_layer_count, neurons_on_hidden_layer_count, f_sigmoid, fp_sigmoid))
        self.layers.append(Layer(neurons_on_hidden_layer_count, output_count, f_identity, fp_identity))

    def __getitem__(self, item):
        return self.layers[item]

    def __len__(self):
        return len(self.layers)

    def work(self, inputs):
        for layer in self:
            inputs = layer.work(inputs)
        return inputs


class Layer:

    def __init__(self, weights_count: int, neurons_count: int, function, derived_function):
        self.neurons = [Neuron(weights_count, function, derived_function) for _ in range(neurons_count)]

    def __getitem__(self, item):
        return self.neurons[item]

    def __len__(self):
        return len(self.neurons)

    def work(self, inputs):
        ret = []
        for neuron in self:
            ret.append(neuron.work(inputs))
        return ret


class Neuron:

    def __init__(self, weight_count: int, function, derived_function):
        self.function = function
        self.derived_function = derived_function

        self.weights = [random.uniform(0.0, 1.0) for _ in range(weight_count)]
        self.previousWeights = [0 for _ in range(weight_count)]
        self.bias = random.uniform(0.0, 1.0)
        self.previousBias = 0

        self.recent_value = 0
        self.derived_value = 0
        self.error = 0

    def __getitem__(self, item):
        return self.weights[item]

    def __setitem__(self, key, value):
        self.weights[key] = value

    def __len__(self):
        return len(self.weights)

    def work(self, inputs: []):
        s = 0
        for i, weight in enumerate(self):
            s += weight * inputs[i]
        s += self.bias
        self.recent_value = self.function(s)
        self.derived_value = self.derived_function(s)
        return self.recent_value
