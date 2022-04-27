import pickle


def input_number(message: str, error: str):
    try:
        value = int(input(message))
        return value
    except ValueError:
        if error:
            print(error)
        return input_number(message, error)


def input_range(message: str, start: int, end: int, error: str):
    value = start - 1
    while value < start or value > end:
        value = input_number(message, error)
        if value >= start and value <= end:
            break
        if error:
            print(error)

    return value


def save_data(data, path):
    with open(path, 'wb') as file:
        pickle.dump(data, file)


def load_data(path):
    with open(path, 'rb') as file:
        return pickle.load(file)
