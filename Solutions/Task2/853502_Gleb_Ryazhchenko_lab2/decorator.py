import random
import math


def decorator(function):
    cache = {}

    def decorate(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            try:
                value = function(*args, **kwargs)
            except Exception:
                raise ValueError
            cache[key] = value
            return value
        else:
            print('Done!')
            return cache[key]

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
