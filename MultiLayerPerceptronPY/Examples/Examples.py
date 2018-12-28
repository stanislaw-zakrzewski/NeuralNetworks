import random

from DataHandling.FileReader import read_classification
from Examples.Example import Example


class Examples:
    def __init__(self, path: str, inputs_count: int, output_count: int):
        self.examples = []
        for e in read_classification(path, inputs_count, output_count):
            self.examples.append(Example(e[0], e[1]))

    def get_random_example(self):
        return random.sample(self.examples)

    def get_example(self, index: int):
        return self.examples[index]
