import random


def numbers():
    mynumbers = [random.randint(0, 10) for _ in range(5)]
    return mynumbers


while True:
    print(numbers())
