from NetworkComponents.Layer import Layer
from Functions import f_identity


class Network:

    def __init__(self, input_count: int, output_count: int, hidden_layers_count: int,
                 neurons_on_hidden_layer_count: int):
        self.layers = []
        self.layers.append(Layer(input_count, neurons_on_hidden_layer_count, f_identity))
        for i in range(hidden_layers_count-1):
            self.layers.append(Layer(neurons_on_hidden_layer_count, neurons_on_hidden_layer_count, f_identity))
        self.layers.append(Layer(neurons_on_hidden_layer_count, output_count, f_identity))

    def work(self, inputs):
        for hl in self.layers:
            inputs = hl.work(inputs)
        return inputs

