from Lab2.parser import parse
from Lab2.from_json import to_string


def lex_string(string):
    json_string = ''

    if string[0] == '"':
        string = string[1:]
    else:
        return None, string

    for c in string:
        if c == '"':
            return json_string, string[len(json_string) + 1:]
        else:
            json_string += c

    raise Exception('Expected end-of-string quote')


def lex_number(string):
    json_number = ''

    number_characters = [str(d) for d in range(0, 10)] + ['-', 'e', '.']

    for c in string:
        if c in number_characters:
            json_number += c
        else:
            break

    rest = string[len(json_number):]

    if not len(json_number):
        return None, string

    if '.' in json_number:
        return float(json_number), rest

    return int(json_number), rest


def lex_bool(string):
    string_len = len(string)

    if string_len >= len('true') and \
            string[:len('true')] == 'true':
        return True, string[len('true'):]
    elif string_len >= len('false') and \
            string[:len('false')] == 'false':
        return False, string[len('false'):]

    return None, string


def lex_null(string):
    string_len = len(string)

    if string_len >= len('null') and \
            string[:len('null')] == 'null':
        return True, string[len('null')]

    return None, string


def lex(string):
    tokens = []

    while len(string):
        json_string, string = lex_string(string)
        if json_string is not None:
            tokens.append(json_string)
            continue

        json_number, string = lex_number(string)
        if json_number is not None:
            tokens.append(json_number)
            continue

        json_bool, string = lex_bool(string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue

        json_null, string = lex_null(string)
        if json_null is not None:
            tokens.append(None)
            continue

        c = string[0]

        if c in [' ', '\t', '\b', '\n', '\r']:
            # Ignore whitespace
            string = string[1:]
        elif c in [',', ':', '[', ']', '{', '}']:
            tokens.append(c)
            string = string[1:]
        else:
            raise Exception('Unexpected character: {}'.format(c))

    return tokens


def from_string(string):
    tokens = lex(string)
    return parse(tokens, is_root=True)[0]


def main():
    print("Normal string:", to_string({"array": [1, 2, 3], "boolean": True, "color": "gold",
                                       "number": 123, "object": {"a": "b", "c": "d"}, "string": "Hello World"}))
    print("JSON string:", from_string(to_string({"array": [1, 2, 3], "boolean": True, "color": "gold",
                                                 "number": 123, "object": {"a": "b", "c": "d"},
                                                 "string": "Hello World"})))


if __name__ == "__main__":
    main()
