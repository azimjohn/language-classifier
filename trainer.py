from threading import Thread
from typing import List, Tuple

from perceptron import Perceptron
from vector import Vector


class Trainer:
    def __init__(
            self,
            perceptrons: List[Perceptron],
            training_data: List[Tuple[str, Vector]],
    ):
        self.perceptrons = perceptrons
        self.training_data = training_data

    def train_parallel(self, learning_rate: float, iterations: int):
        threads = []

        for perceptron in self.perceptrons:
            args = (self.training_data, learning_rate, iterations)
            thread = Thread(target=perceptron.train, args=args, name=perceptron.label)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
