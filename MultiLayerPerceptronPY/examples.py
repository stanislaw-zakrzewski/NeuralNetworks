import random


class Examples:
    def __init__(self, path: str, inputs_count: int, output_count: int):
        self.examples = []
        for e in read_classification(path, inputs_count, output_count):
            self.examples.append(Example(e[0], e[1]))

    def __getitem__(self, item):
        return self.examples[item]

    def __setitem__(self, key, value):
        self.examples[key] = value

    def __len__(self):
        return len(self.examples)

    def random(self):
        return random.choice(self.examples)


class Example:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs


def read_classification(path: str, inputs_count: int, outputs_count: int):
    file = open(path, "r")
    ret = []
    for x in file:
        inputs = []
        outputs = []
        s = x.split(" ")
        counter = 0
        for i in range(inputs_count):
            inputs.append(float(s[counter]))
            counter += 1
        for i in range(outputs_count):
            outputs.append(float(s[counter]))
            counter += 1
        ret.append([inputs, outputs])
    return ret
