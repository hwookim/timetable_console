from utils import *


def manage_timetable(timetable=[], lectures=[], rooms=[]):
    data = timetable
    value = 0
    while value != 5:
        print_menu()
        value = input_number('> ', '1 ~ 4 사이의 수를 입력해주세요.')
        if value == 1:
            print()
        elif value == 2:
            print()
        elif value == 3:
            print()
        elif value == 4:
            break
        else:
            print('1 ~ 4 사이의 수를 입력해주세요.')

    return data


def print_menu():
    print()
    print('**********************************************************************')
    print('1. 시간표 출력')
    print('2. 강의 등록')
    print('3. 강의 삭제')
    print('4. 나가기')
    print('**********************************************************************')
