def parse_array(tokens):
    json_array = []

    t = tokens[0]
    if t == ']':
        return json_array, tokens[1:]

    while True:
        json, tokens = parse(tokens)
        json_array.append(json)

        t = tokens[0]
        if t == ']':
            return json_array, tokens[1:]
        elif t != ',':
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]
    raise Exception('Expected end-of-array bracket')


def parse_object(tokens):
    json_object = {}

    t = tokens[0]
    if t == '}':
        return json_object, tokens[1:]

    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception('Expected string key, got: {}'.format(json_key))

        t = tokens[0]
        if t != ':':
            raise Exception('Expected colon after key in object, got: {}'.format(t))

        json_value, tokens = parse(tokens[1:])

        json_object[json_key] = json_value

        t = tokens[0]
        if t == '}':
            return json_object, tokens[1:]
        elif t != ',':
            raise Exception('Expected comma after pair in object, got: {}'.format(t))

        tokens = tokens[1:]
    raise Exception('Expected end-of-object bracket')


def parse(tokens, is_root=False):
    t = tokens[0]

    if is_root and t != '{':
        raise Exception('Root must be an object')

    if t == '[':
        return parse_array(tokens[1:])
    elif t == '{':
        return parse_object(tokens[1:])
    else:
        return t, tokens[1:]
