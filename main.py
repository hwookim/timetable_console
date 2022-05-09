from utils import *
from constants import *

from manage_subjects import manageSubjects
from manage_lectures import manage_lectures
from manage_rooms import mainRoom
from manage_timetable import manage_timetable
from manage_data import manage_data


_subjects = [{SUBJECT_CODE: 'MME', SUBJECT_NAME: '자율사물기초프로그래밍',
              SUBJECT_GRADE: '1', SUBJECT_SEM: '1', SUBJECT_EX: '파이썬'}]
_lectures = {'MME-01': {TEACHER: '성연식',
                        SUBJECT_CODE: 'MME', YEAR: '2022', SEMESTER: '1'}}
_rooms = [{ROOM_CODE: '4105', ROOM_NAME: '4105', ROOM_CAPACITY: '40'}]
_timetable = {
    '2022': {
        '1': [
            {TIMETABLE_DAY: DAYS[0], TIMETABLE_TIME: '09:00~11:00',
                TIMETABLE_ROOM: '4105', TIMETABLE_LECTURE: 'MME-01'},
            {TIMETABLE_DAY: DAYS[2], TIMETABLE_TIME: '14:00~16:30',
                TIMETABLE_ROOM: '4105', TIMETABLE_LECTURE: 'MME-01'}
        ]
    }
}


def main():
    global _subjects
    global _lectures
    global _rooms
    global _timetable

    value = 0
    while value != 7:
        print_menu()
        value = input_number('> ', '1 ~ 6 사이의 수를 입력해주세요.')
        if value == 1:
            manageSubjects(_subjects)
        elif value == 2:
            manage_lectures(_lectures, _subjects)
        elif value == 3:
            mainRoom()
        elif value == 4:
            manage_timetable(_timetable, _subjects, _lectures, _rooms)
        elif value == 5:
            manage_data(_subjects, _lectures, _rooms, _timetable)
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


main()
