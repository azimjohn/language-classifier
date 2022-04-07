from selector import Selector
from perceptron import Perceptron, sigmoid
from trainer import Trainer
from reader import *


LEARNING_RATE = 0.02
ITERATIONS = 20


if __name__ == '__main__':
    training_data = list(load_data("./data/train"))
    test_data = list(load_data("./data/test"))
    default_weight = Vector([0.1] * DIMENSIONS)

    perceptron_en = Perceptron("English", default_weight.copy())
    perceptron_de = Perceptron("German", default_weight.copy())
    perceptron_pl = Perceptron("Polish", default_weight.copy())
    perceptron_uz = Perceptron("Uzbek", default_weight.copy())

    perceptrons = [perceptron_en, perceptron_de, perceptron_pl, perceptron_uz]

    trainer = Trainer(perceptrons, training_data)
    trainer.train_parallel(LEARNING_RATE, ITERATIONS)
    selector = Selector(perceptrons, activation_func=sigmoid)

    total = 0
    correct = 0
    for expected, vector in test_data:
        prediction = selector.select(vector)
        if prediction == expected:
            correct += 1
        total += 1

    print("Accuracy of selector: ", round(correct/total, 2))

    text = sanitize(multiline_input("Enter text to detect language: "))
    vector = build_vector(text).normalize()
    print("Language: ", selector.select(vector))
