from re import sub
from utils import *

from manage_lectures import manage_lectures
from manage_timetable import manage_timetable


subjects = []
lectures = []
rooms = []
timetable = []


def main():
    value = 0
    while value != 7:
        print_menu()
        value = input_number('> ', '1 ~ 6 사이의 수를 입력해주세요.')
        if value == 1:
            manage_subjects()
        elif value == 2:
            manage_lectures(lectures, subjects)
        elif value == 3:
            manage_rooms()
        elif value == 4:
            manage_timetable(timetable, lectures, rooms)
        elif value == 5:
            manage_data()
        elif value == 6:
            print()
            print('프로그램을 종료합니다.')
            break
        else:
            print('1 ~ 6 사이의 수를 입력해주세요.')


def print_menu():
    print()
    print('**********************************************************************')
    print('1. 교과목 관리')
    print('2. 강의 관리')
    print('3. 강의실 관리')
    print('4. 시간표 관리')
    print('5. 데이터 관리')
    print('6. 종료')
    print('**********************************************************************')


def manage_subjects():
    print()


def manage_rooms():
    print()


def manage_data():
    print()


main()
