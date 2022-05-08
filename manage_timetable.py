from utils import *
from constants import *


def manage_timetable(timetable=[], subjects=[], lectures=[], rooms=[]):
    global _timetable
    global _subjects
    global _lectures
    global _rooms
    _timetable = timetable
    _subjects = subjects
    _lectures = lectures
    _rooms = rooms

    value = 0
    while value != 5:
        print_menu()
        value = input_number('> ', '1 ~ 4 사이의 수를 입력해주세요.')
        if value == 1:
            print_timetable()
        elif value == 2:
            print()
        elif value == 3:
            print()
        elif value == 4:
            break
        else:
            print('1 ~ 4 사이의 수를 입력해주세요.')


def print_menu():
    print()
    print('**********************************************************************')
    print('1. 시간표 출력')
    print('2. 강의 등록')
    print('3. 강의 삭제')
    print('4. 나가기')
    print('**********************************************************************')


def print_timetable():
    print()
    if not len(_timetable) > 0:
        print('시간표에 등록된 강의가 없습니다.')
        return

    print_timetable_in_range_time(0, 6)
    print_timetable_in_range_time(6.5, 12.5)


def print_timetable_in_range_time(start=0, end=6):
    cnt = 0
    boundary_time = TIMES[(int)(start * 2):(int)(end * 2 + 1)]
    print(center_consider_kor('시간', 20), end=' |')
    for time in boundary_time:
        print(center_consider_kor(time, 10), end='|')
    print()

    print(center_consider_kor('요일', 10) + '|' + center_consider_kor('강의실', 10))
    for day in _timetable:
        print('-' * 175)
        print(center_consider_kor(day, 10), end='|')
        for room in _timetable[day]:
            print(center_consider_kor(room, 10), end='|')
            for index, time in enumerate(boundary_time):
                if not time in _timetable[day][room]:
                    if cnt != 0:
                        lecture_code = _timetable[day][room][TIMES[index - 1]]
                        lecture_info = get_lecture_info(lecture_code)
                        print(
                            center_consider_kor(
                                lecture_info, 10 * cnt + cnt - 1),
                            end='|'
                        )
                        cnt = 0
                    print(' ' * 10, end='|')
                else:
                    if cnt != 0:
                        cnt += 1
                        continue
                    cnt = 1
        print()
    print('-' * 175)
    print()


def get_lecture_info(lecture_code):
    subject_id = _lectures[lecture_code][SUBJECT_ID]
    subject_name = _subjects[subject_id][SUBJECT_NAME]
    teacher_name = _lectures[lecture_code][TEACHER]
    return '{0}({1})'.format(subject_name[0:10], teacher_name[0:3])


'''
실행 예시
- 데이터 변경 필요
manage_timetable(
    {
        DAYS[0]: {'4105': {
            TIMES[0]: 'MME-01',
            TIMES[1]: 'MME-01',
            TIMES[2]: 'MME-01',
        }},
        DAYS[1]: {'4105': {}},
        DAYS[2]: {'4105': {}},
        DAYS[3]: {'4105': {}},
        DAYS[4]: {'4105': {}}
    },
    {'MME': {'교과목명': '자율사물기초프로그래밍'}},
    {'MME-01': {'교원명': '성연식', '교과목 코드': 'MME'}}
)

'''
