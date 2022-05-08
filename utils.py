import unicodedata
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


def rjust_consider_kor(value="", max_size=10, fill_char=" "):
    l = 0
    for c in value:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l += 2
        else:
            l += 1
    return fill_char * (max_size - l) + value


def ljust_consider_kor(value="", max_size=10, fill_char=" "):
    l = 0
    for c in value:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l += 2
        else:
            l += 1
    return value + fill_char * (max_size - l)


def center_consider_kor(value="", max_size=10, fill_char=" "):
    l = 0
    for c in value:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l += 2
        else:
            l += 1
    result = fill_char * (int)((max_size - l) / 2) + value + \
        fill_char * (int)((max_size - l) / 2)
    if (max_size - l) % 2 != 0:
        return ' ' + result
    return result
