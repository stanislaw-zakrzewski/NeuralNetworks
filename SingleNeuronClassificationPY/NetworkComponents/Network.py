from NetworkComponents import Neuron


class Network:
    def __init__(self, input_count):
        self.neuron = Neuron.Neuron(input_count)
        self.input_count = input_count
        self.learning_rate = 0.01

    def work(self, inputs):
        result = 0
        for i in range(len(inputs)):
            result += self.neuron.get_weights()[i] * inputs[i]
        if result > 0.5:
            return 1
        else:
            return 0

    def adapt(self, example):
        result = self.work(example.getInputs())
        result_offset = example.desired_result - result

        for i in range(self.input_count):
            weight_change = result_offset * (- example.getInputs()[i])
            self.neuron.get_weights()[i] -= self.learning_rate * weight_change
