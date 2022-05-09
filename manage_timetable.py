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
        value = input_number('> ', '1 ~ 5 사이의 수를 입력해주세요.')
        if value == 1:
            print()
            year, semester = select_year_semester()
            print_timetable(year, semester)
        elif value == 2:
            input_timetable()
        elif value == 3:
            update_timetable()
        elif value == 4:
            delete_timetable()
        elif value == 5:
            break
        else:
            print('1 ~ 5 사이의 수를 입력해주세요.')


def print_menu():
    print()
    print('**********************************************************************')
    print('1. 시간표 출력')
    print('2. 강의 등록')
    print('3. 강의 수정')
    print('4. 강의 삭제')
    print('5. 나가기')
    print('**********************************************************************')


def print_timetable(year, semester):
    print()
    if not len(_timetable) > 0:
        print('강의가 등록된 시간표가 없습니다.')
        return

    target = _timetable[year][semester]
    if not len(target) > 0:
        print('해당 시기의 시간표에 등록된 강의가 없습니다.')
        return

    timetable = convert_timetable(target)

    print_timetable_in_range_time(timetable, 0, 6)
    print_timetable_in_range_time(timetable, 6.5, 12.5)


def select_year_semester():
    year = str(input_range(ljust_consider_kor(YEAR, 10) + '> ',
                           2000, 3000, '올바른 년도를 입력해주세요.'))
    semester = str(input_range(ljust_consider_kor(SEMESTER, 10) + '> ',
                               1, 2, '올바른 학기를 입력해주세요.'))
    return year, semester


def convert_timetable(timetable):
    result = {
        DAYS[0]: {},
        DAYS[1]: {},
        DAYS[2]: {},
        DAYS[3]: {},
        DAYS[4]: {},
    }

    for item in timetable:
        day = item[TIMETABLE_DAY]
        room_code = item[TIMETABLE_ROOM]
        times = item[TIMETABLE_TIME]
        lecture_code = item[TIMETABLE_LECTURE]

        if not room_code in result[day]:
            result[day][room_code] = {}

        start, end = times.split('~')
        for time in range(TIMES.index(start), TIMES.index(end)):
            result[day][room_code][TIMES[time]] = lecture_code

    return result


def print_timetable_in_range_time(timetable, start, end):
    cnt = 0
    start_index = (int)(start * 2)
    end_index = (int)(end * 2 + 1)
    boundary_time = TIMES[start_index:end_index]
    print(center_consider_kor('시간', 20), end=' |')
    for time in boundary_time:
        print(center_consider_kor(time, 10), end='|')
    print()

    print(center_consider_kor('요일', 10) + '|' + center_consider_kor('강의실', 10))
    for day in timetable:
        print('-' * 175)
        print(center_consider_kor(day, 10), end='|')
        for room in timetable[day]:
            print(center_consider_kor(room, 10), end='|')
            for index, time in enumerate(boundary_time):
                if not time in timetable[day][room]:
                    if cnt != 0:
                        lecture_code = timetable[day][room][TIMES[index - 1 + start_index]]
                        lecture_info = get_lecture_info(
                            lecture_code, cnt)
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
            if cnt != 0:
                lecture_code = timetable[day][room][TIMES[end_index - 1]]
                lecture_info = get_lecture_info(
                    lecture_code, cnt)
                print(
                    center_consider_kor(
                        lecture_info, 10 * cnt + cnt - 1),
                    end='|'
                )
                cnt = 0
        print()
    print('-' * 175)
    print()


def get_lecture_info(lecture_code, space):
    subject_code = _lectures[lecture_code][SUBJECT_CODE]
    for subject in _subjects:
        if subject[SUBJECT_CODE] == subject_code:
            subject_name = subject[SUBJECT_NAME]
    teacher_name = _lectures[lecture_code][TEACHER]
    if space <= 2:
        return '{0}({1})'.format(subject_name[0:space*3], teacher_name[0:1])
    return '{0}({1})'.format(subject_name[0:space*5], teacher_name[0:3])


def input_timetable():
    print()
    year, semester = select_year_semester()
    if not year in _timetable:
        _timetable[year] = {}
    if not semester in _timetable[year]:
        _timetable[year][semester] = {}

    print_timetable(year, semester)

    target = _timetable[year][semester]
    comparison_target = convert_timetable(target)

    while True:
        flag = False

        room_code = input_room_code()
        day, times = input_time()
        if not room_code in comparison_target[day]:
            comparison_target[day][room_code] = {}
            break
        start, end = times.split('~')
        for time in range(TIMES.index(start), TIMES.index(end)):
            if TIMES[time] in comparison_target[day][room_code]:
                flag = True
                break
        if flag:
            print('해당 강의실의 해당 시간에 이미 존재하는 강의가 있습니다.')
        else:
            break

    lecture_code = input_lecture_code()
    target.append({
        TIMETABLE_DAY: day,
        TIMETABLE_TIME: times,
        TIMETABLE_ROOM: room_code,
        TIMETABLE_LECTURE: lecture_code
    })


def input_room_code():
    while True:
        room_code = input(ljust_consider_kor('강의실 코드', 15) + '> ')

        for room in _rooms:
            if room[ROOM_CODE] == room_code:
                return room_code

        print('해당하는 강의실이 없습니다.')


def input_time():
    while True:
        flag = False
        day_times = input('강의 요일/시간 (ex.월요일/09:00~11:00) > ')
        day, times = day_times.split('/')
        if not day in DAYS:
            break
        start, end = times.split('~')
        if not start in TIMES or not end in TIMES:
            break
        return day, times

    print('잘못 입력하셨습니다.')
    print('요일/시작시간~종료시간 (ex.월요일/09:00~11:00)의 형태로 입력해주세요.')
    return input_time()


def input_lecture_code():
    while True:
        lecture_code = input(ljust_consider_kor('강의 코드', 15) + '> ')

        if lecture_code in _lectures.keys():
            return lecture_code

        print('해당하는 강의가 없습니다.')


def update_timetable():
    if not len(_timetable) > 0:
        print('강의가 등록된 시간표가 없습니다.')
        return

    year, semester = select_year_semester()
    target = _timetable[year][semester]
    if not len(target) > 0:
        print('해당 시기의 시간표에 등록된 강의가 없습니다.')
        return


def delete_timetable():
    if not len(_timetable) > 0:
        print('강의가 등록된 시간표가 없습니다.')
        return

    year, semester = select_year_semester()
    target = _timetable[year][semester]
    if not len(target) > 0:
        print('해당 시기의 시간표에 등록된 강의가 없습니다.')
        return
