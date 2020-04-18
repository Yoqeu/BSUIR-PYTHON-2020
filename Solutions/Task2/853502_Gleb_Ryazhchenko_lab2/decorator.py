import random
import math


def decorator(function):
    cache = {}

    def decorate(*args):
        if args in cache:
            print("Decorator worked!")
            return cache[args]
        else:
            cache[args] = function(*args)
            return cache[args]

    return decorate


@decorator
def logarifm(x):
    return math.log(x, 2)


def main():
    for i in range(10):
        x = random.randint(1, 10)
        print("log(", x, ") = ", logarifm(x))


if __name__ == "__main__":
    main()
