import math
from typing import Callable, Iterable, Tuple

from vector import Vector


def sigmoid(net):
    return 1 / (1 + math.e ** -net)


def step(net):
    return 1 if net > 0 else 0


class Perceptron:
    def __init__(self, label: str, initial_weight: Vector, initial_bias: float = 0, ):
        self.label = label
        self.bias = initial_bias
        self.weight_vector = initial_weight

    def output_value(self, x: Vector, activation_func: Callable = None) -> bool:
        activation_func = activation_func or step
        net = self.weight_vector * x - self.bias
        return activation_func(net)

    def train(
            self,
            training_data: Iterable[Tuple[str, Vector]],
            learning_rate: float,
            iterations: int,
    ) -> None:
        for _ in range(iterations):
            for label, x in training_data:
                y = self.output_value(x)
                d = label == self.label
                err = d - y

                self.weight_vector += x * (err * learning_rate)
                self.bias -= err * learning_rate
