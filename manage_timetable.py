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
            print()
        elif value == 5:
            break
        else:
            print('1 ~ 4 사이의 수를 입력해주세요.')


def print_menu():
    print()
    print('**********************************************************************')
    print('1. 시간표 출력')
    print('2. 강의 등록')
    print('3. 강의 수정')
    print('4. 강의 삭제')
    print('5. 나가기')
    print('**********************************************************************')


def print_timetable():
    print()
    if not len(_timetable) > 0:
        print('시간표에 등록된 강의가 없습니다.')
        return

    year = str(input_range(ljust_consider_kor(YEAR, 10) + '> ',
                           2000, 3000, '올바른 년도를 입력해주세요.'))
    semester = str(input_range(ljust_consider_kor(SEMESTER, 10) + '> ',
                               1, 2, '올바른 학기를 입력해주세요.'))
    if not len(_timetable[year][semester]) > 0:
        print('해당 시기의 시간표에 등록된 강의가 없습니다.')
        return

    print_timetable_in_range_time(year, semester, 0, 6)
    print_timetable_in_range_time(year, semester, 6.5, 12.5)


def print_timetable_in_range_time(year, semester, start, end):
    timetalbe = _timetable[year][semester]
    cnt = 0
    boundary_time = TIMES[(int)(start * 2):(int)(end * 2 + 1)]
    print(center_consider_kor('시간', 20), end=' |')
    for time in boundary_time:
        print(center_consider_kor(time, 10), end='|')
    print()

    print(center_consider_kor('요일', 10) + '|' + center_consider_kor('강의실', 10))
    for day in timetalbe:
        print('-' * 175)
        print(center_consider_kor(day, 10), end='|')
        for room in timetalbe[day]:
            print(center_consider_kor(room, 10), end='|')
            for index, time in enumerate(boundary_time):
                if not time in timetalbe[day][room]:
                    if cnt != 0:
                        lecture_code = timetalbe[day][room][TIMES[index - 1]]
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
