


class Name(object):
    def __init__(self):
        self.first_name = "John"
        self.second_name = "Abrams"
        self.rty = (1, 2)
        super(Name, self).__init__()


class Person(object):
    def __init__(self):
        self.married = True
        self.mail = None
        self.logic = False
        self.height = 180
        self.qwe = {1, 2, 3}
        self.name = Name()
        super(Person, self).__init__()


def to_string(json):
    json_type = type(json)
    if json_type is dict:
        string = '{'
        dict_len = len(json)

        for i, (key, val) in enumerate(json.items()):
            string += '"{}": {}'.format(key, to_string(val))

            if i < dict_len - 1:
                string += ', '
            else:
                string += '}'

        return string
    elif json_type is list:
        string = '['
        list_len = len(json)

        for i, val in enumerate(json):
            string += to_string(val)

            if i < list_len - 1:
                string += ', '
            else:
                string += ']'

        return string
    elif json_type is str:
        return '"{}"'.format(json)
    elif json_type is bool:
        return 'true' if json else 'false'
    elif json_type is None:
        return 'null'

    return str(json)


def main():
    print("Normal string:", to_string({"array": [1, 2, 3], "boolean": True, "color": "gold",
                                       "number": 123, "object": {"a": "b", "c": "d"}, "string": "Hello World"}))
    

if __name__ == "__main__":
    main()

