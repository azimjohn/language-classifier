import os
from collections import Counter
from pathlib import Path
from typing import Iterator, Tuple

from vector import Vector

DIMENSIONS = 26


def sanitize(text: str) -> Iterator[str]:
    for char in text:
        if char.isalpha():
            yield char.lower()


def build_vector(text: Iterator[str]) -> Vector:
    a = ord('a')
    counter = Counter(text)
    return Vector([counter[chr(a+i)] for i in range(DIMENSIONS)])


def load_datapoint(root: str, path: str) -> Tuple[str, Vector]:
    root = Path(root)
    with open(root / path, encoding='latin-1') as file:
        text = file.read().encode("ascii", "ignore")
        sanitized = sanitize(text.decode())
        vector = build_vector(sanitized)
    return root.name, vector.normalize()


def load_data(root: str):
    for root, dirs, files, in os.walk(root):
        for file in files:
            if file.endswith('.txt'):
                yield load_datapoint(root, file)


def multiline_input(message):
    print(message)
    contents = []
    while True:
        line = input()
        if line.startswith("END"):
            break
        contents.append(line)
    return "\n".join(contents)
