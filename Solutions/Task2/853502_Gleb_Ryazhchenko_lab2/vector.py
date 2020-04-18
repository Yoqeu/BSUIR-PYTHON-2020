import math


class Error(Exception):
    pass


class SmallValueError(Error):
    pass


class OutOfRangeValue(Error):
    pass


class Vector:

    def __init__(self, components):
        if type(components) != tuple or len(components) == 0:
            raise TypeError('components must be a non-empty tuple')
        self._components = components

    def __repr__(self):
        return 'Vector({})'.format(self._components)

    def __len__(self):
        return len(self._components)

    def __bool__(self):
        for component in self._components:
            if component != 0:
                return True

        return False

    def __eq__(self, other):
        if type(other) != Vector:
            return False

        return self._components == other._components

    def __ne__(self, other):
        if type(other) != Vector:
            return True

        return self._components != other._components

    def __add__(self, other):
        if type(other) != Vector:
            raise ValueError('cannot add non-vectors to vectors')
        elif len(self._components) != len(other._components):
            raise ValueError('cannot add vectors of differing dimensions')

        new_components = []

        for i in range(len(self._components)):
            new_components.append(self._components[i] + other._components[i])

        return Vector(tuple(new_components))

    def __sub__(self, other):
        if type(other) != Vector:
            raise ValueError('cannot subtract non-vectors to vectors')
        elif len(self._components) != len(other._components):
            raise ValueError('cannot subtract vectors of differing dimensions')

        new_components = []

        for i in range(len(self._components)):
            new_components.append(self._components[i] - other._components[i])

        return Vector(tuple(new_components))

    def __mul__(self, other):
        if type(other) == Vector:
            if len(self._components) != len(other._components):
                raise ValueError('cannot multiply vectors of differing dimensions')

            dot_product = 0

            for i in range(len(self._components)):
                dot_product += self._components[i] * other._components[i]

            return dot_product

        elif type(other) in [int, float]:
            new_components = []

            for component in self._components:
                new_components.append(component * other)

            return Vector(tuple(new_components))

        else:
            raise TypeError('unsupported type in vector multiplication')

    def __truediv__(self, other):
        if type(other) in [int, float]:
            new_components = []

            for component in self._components:
                new_components.append(component / other)

            return Vector(tuple(new_components))
        else:
            raise TypeError('cannot divide vectors by anything other than numbers')

    def __neg__(self):
        new_components = []

        for component in self._components:
            new_components.append(-component)

        return Vector(tuple(new_components))

    def __pos__(self):
        return self


def show_operations():
    operation = input("\nChoose operation:\n" +
                      "1. Addition\n" +
                      "2. Subtraction\n" +
                      "3. Multiplication by a constant\n" +
                      "4. Scalar multiplication\n" +
                      "5. Comparison\n" +
                      "6. Length of vectors\n" +
                      "7. Exit\n")
    while True:
        try:
            if 0 < int(operation) < 8:
                return int(operation)
            else:
                raise OutOfRangeValue
        except OutOfRangeValue:
            print("Value is out of range!")
            operation = input()


def main():
    while True:
        try:
            dimension = int(input("Input vectors dimension: "))
            if dimension <= 0:
                raise SmallValueError
            else:
                break
        except SmallValueError:
            print("Value is too small!")
    coords = []
    coords_1 = []
    for i in range(int(dimension)):
        coordinate = input(str(i + 1) + ": ")
        coords.append(int(coordinate))
    for i in range(int(dimension)):
        coordinate = input(str(i + 1) + ": ")
        coords_1.append(int(coordinate))
    while True:
        operation = show_operations()
        if operation == 1:
            print("\n", Vector(tuple(coords)), "+", Vector(tuple(coords_1)), "=",
                  Vector.__add__(Vector(tuple(coords)), Vector(tuple(coords_1))))
        elif operation == 2:
            print("\n", Vector(tuple(coords)), "-", Vector(tuple(coords_1)), "=",
                  Vector.__sub__(Vector(tuple(coords)), Vector(tuple(coords_1))))
        elif operation == 3:
            constant = float(input("Input a constant: "))
            print("\n", Vector(tuple(coords)), "*", constant, " = ", Vector.__mul__(Vector(tuple(coords)), constant),
                  '\n', Vector(tuple(coords_1)), "*", constant, " = ",
                  Vector.__mul__(Vector(tuple(coords_1)), constant))
        elif operation == 4:
            print("\n", Vector(tuple(coords)), "*", Vector(tuple(coords_1)), "=",
                  Vector.__mul__(Vector(tuple(coords)), Vector(tuple(coords_1))))
        elif operation == 5:
            if Vector.__eq__(Vector(tuple(coords)), Vector(tuple(coords_1))):
                print("\nVector ", Vector(tuple(coords)), "is equal vector ", Vector(tuple(coords_1)))
            else:
                print("\nVector ", Vector(tuple(coords)), "is NOT equal vector ", Vector(tuple(coords_1)))
        elif operation == 6:
            print("\nThe length of ", Vector(tuple(coords)), " vector = ",
                  "{:1.4f}".format(Vector.__len__(Vector(tuple(coords)))),
                  "\n")
            print("The length of ", Vector(tuple(coords_1)), " vector = ",
                  "{:1.4f}".format(Vector.__len__(Vector(tuple(coords_1)))),
                  "\n")
        elif operation == 7:
            quit()


if __name__ == "__main__":
    main()
