import random

from network_components import Network
from examples import Examples


def train(network: Network, examples: Examples, epochs: int, initial_learning_rate, momentum):
    for i in range(epochs):
        random.shuffle(examples)
        sqrt_error = 0.0
        for example in examples:
            network.work(example.inputs)
            sqrt_error += calculate_errors(network, example.outputs)
            learning_rate = initial_learning_rate * ((epochs - i) / epochs)
            update_weights(network, example.inputs, learning_rate, momentum)
        print(sqrt_error / len(examples))


def calculate_errors(network, desired_outputs):
    sqrt_error = 0

    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron[j] * neuron.error)
                errors.append(error)
        else:
            for j, neuron in enumerate(layer):
                errors.append(desired_outputs[j] - neuron.recent_value)
        for j, neuron in enumerate(layer):
            neuron.error = errors[j] * neuron.derived_value

    for neuron in network[len(network) - 1]:
        sqrt_error += 1 / 2 * (neuron.error ** 2)

    return sqrt_error


def update_weights(network, inputs, learning_rate, momentum):
    for i in range(len(network)):
        if i != 0:
            inputs = [neuron.recent_value for neuron in network[i - 1].neurons]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron.previousWeights[j] = neuron[j]
                neuron[j] += 2 * learning_rate * neuron.error * inputs[j]
                neuron[j] += momentum * (neuron[j] - neuron.previousWeights[j])
            neuron.previousBias = neuron.bias
            neuron.bias += 2 * learning_rate * neuron.error + momentum * (neuron.bias - neuron.previousBias)
