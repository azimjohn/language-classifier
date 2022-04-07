from typing import List, Callable

from perceptron import Perceptron
from vector import Vector


class Selector:
    def __init__(self, perceptrons: List[Perceptron], activation_func: Callable) -> None:
        self.perceptrons = perceptrons
        self.activation_func = activation_func

    def select(self, vector: Vector) -> str:
        result = ""
        max_output = -1

        for perceptron in self.perceptrons:
            output = perceptron.output_value(vector, activation_func=self.activation_func)
            if output > max_output:
                max_output = output
                result = perceptron.label

        return result
