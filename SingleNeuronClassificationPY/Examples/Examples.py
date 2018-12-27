from DataHandling import FileReader
from Examples import Example
import numpy as np


class Examples:
    def __init__(self, path):
        self.examples = []
        examples_dataset = FileReader.read_file(path)
        for x in examples_dataset:
            self.examples.append(Example.Example(x[0], x[1], x[2]))

    def get_random_example(self):
        return np.random.choice(self.examples)

    def get_specific_example(self, index):
        return self.examples[index]
