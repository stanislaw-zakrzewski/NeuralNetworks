from network_components import Network
from examples import Examples


def train(network: Network, examples: Examples, epochs: int):
    for i in range(epochs):
        example = examples.random()
        network.work(example.inputs)
        calculate_errors(network, example.outputs)
        learning_rate = 0.3 * ((epochs - i) / epochs)
        update_weights(network, example.inputs, learning_rate)


def calculate_errors(network, desired_outputs):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1].neurons:
                    error += (neuron[j] * neuron.error)
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(desired_outputs[j] - neuron.recent_value)
        for j in range(len(layer)):
            neuron = layer[j]
            neuron.error = errors[j] * neuron.derived_value


def update_weights(network, row, learning_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron.recent_value for neuron in network[i - 1].neurons]
        for neuron in network[i].neurons:
            for j in range(len(inputs)):
                neuron[j] += learning_rate * neuron.error * inputs[j]
            neuron.bias += learning_rate * neuron.error
