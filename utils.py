import unicodedata
import pickle


def input_number(message: str, error: str):
    '''숫자 입력

    숫자 외의 값이 들어오면 재입력하도록 함.

    Args:
        message: input 안에 들어갈 메시지
        error: 숫자가 아닐 때 출력된 메시지

    Returns:
        입력된 숫자
    '''
    try:
        value = int(input(message))
        return value
    except ValueError:
        if error:
            print(error)
        return input_number(message, error)


def input_range(message: str, start: int, end: int, error: str):
    '''범위 내 숫자 입력

    범위 외의 숫자 값이 들어오면 재입력하도록 함.

    Args:
        message: input 안에 들어갈 메시지
        error: 범위 내의 숫자가 아닐 때 출력된 메시지

    Returns:
        입력된 숫자
    '''
    value = start - 1
    while value < start or value > end:
        value = input_number(message, error)
        if value >= start and value <= end:
            break
        if error:
            print(error)

    return value


def save_data(data, path):
    '''파일 저장

    데이터를 해당 경로에 저장

    Args:
        data: 저장할 대상 데이터
        path: 저장할 파일의 경로
    '''
    with open(path, 'wb') as file:
        pickle.dump(data, file)


def load_data(path):
    '''파일 로드

    경로 상의 파일의 데이터를 읽어옴

    Args:
        path: 저장된 파일의 경로

    Returns:
        불러온 데이터
    '''
    with open(path, 'rb') as file:
        return pickle.load(file)


def rjust_consider_kor(value="", max_size=10, fill_char=" "):
    '''한글을 고려한 채우기와 함께 우측정렬

    필요한 만큼 특정 문자를 채운 뒤 문자를 우측 정렬.
    이 때 한글은 2칸을 차지함을 고려함

    Args:
        value: 정렬할 문자열
        max_size: 넓이, 기본 10
        fill_char: 채우기 문자, 기본 공백

    Returns:
        크기만큼의 넓이를 가진 우측정렬된 문자열
    '''
    l = 0
    for c in value:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l += 2
        else:
            l += 1
    return fill_char * (max_size - l) + value


def ljust_consider_kor(value="", max_size=10, fill_char=" "):
    '''한글을 고려한 채우기와 함께 좌측정렬

    필요한 만큼 특정 문자를 채운 뒤 문자를 좌측 정렬.
    이 때 한글은 2칸을 차지함을 고려함

    Args:
        value: 정렬할 문자열
        max_size: 넓이, 기본 10
        fill_char: 채우기 문자, 기본 공백

    Returns:
        크기만큼의 넓이를 가진 좌측정렬된 문자열
    '''
    l = 0
    for c in value:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l += 2
        else:
            l += 1
    return value + fill_char * (max_size - l)


def center_consider_kor(value="", max_size=10, fill_char=" "):
    '''한글을 고려한 채우기와 함께 중앙정렬

    필요한 만큼 특정 문자를 채운 뒤 문자를 중앙 정렬.
    이 때 한글은 2칸을 차지함을 고려함

    Args:
        value: 정렬할 문자열
        max_size: 넓이, 기본 10
        fill_char: 채우기 문자, 기본 공백

    Returns:
        크기만큼의 넓이를 가진 중앙정렬된 문자열
    '''
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
