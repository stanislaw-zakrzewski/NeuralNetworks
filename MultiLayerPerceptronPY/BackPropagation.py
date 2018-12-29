learning_rate = 0.3


def train_network(network, inputs, expected):
    network.work(inputs)
    calculate_errors(network, expected)
    update_weights(network, inputs)


def calculate_errors(network, desired_outputs):
    for i in reversed(range(len(network.layers))):
        layer = network.layers[i]
        errors = list()
        if i != len(network.layers) - 1:
            for j in range(len(layer.neurons)):
                error = 0.0
                for neuron in network.layers[i + 1].neurons:
                    error += (neuron.weights[j] * neuron.error)
                errors.append(error)
        else:
            for j in range(len(layer.neurons)):
                neuron = layer.neurons[j]
                errors.append(desired_outputs[j] - neuron.recent_value)
        for j in range(len(layer.neurons)):
            neuron = layer.neurons[j]
            neuron.error = errors[j] * neuron.derived_value


def update_weights(network, row):
    for i in range(len(network.layers)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron.recent_value for neuron in network.layers[i - 1].neurons]
        for neuron in network.layers[i].neurons:
            for j in range(len(inputs)):
                neuron.weights[j] += learning_rate * neuron.error * inputs[j]
            neuron.bias += learning_rate * neuron.error
