class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class TestClass(metaclass=Singleton):
    pass


def main():
    first_object = TestClass()
    print("First object created. It's address:  ", first_object)
    second_object = TestClass()
    print("Second object created. It's address: ", second_object)


if __name__ == '__main__':
    main()
