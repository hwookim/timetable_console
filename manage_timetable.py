from utils import *
from constants import *


def manage_timetable(timetable={}, subjects=[], lectures={}, rooms=[]):
    '''시간표 관리

    Args:
        timetable: 시간표 dict
        subjects: 교과목 array
        lectures: 강의 dict
        rooms: 강의실 array
    '''
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
            if not len(_timetable) > 0:
                print('강의가 등록된 시간표가 없습니다.')
                break
            year, semester = select_year_semester()
            print_timetable(year, semester)
        elif value == 2:
            print()
            year, semester = select_year_semester()
            data = input_timetable(year, semester)
            _timetable[year][semester].append(data)
        elif value == 3:
            update_timetable()
        elif value == 4:
            delete_timetable()
        elif value == 5:
            break
        else:
            print('1 ~ 5 사이의 수를 입력해주세요.')


def print_menu():
    '''시간표 관리 메뉴 출력
    '''
    print()
    print('**********************************************************************')
    print('1. 시간표 출력')
    print('2. 강의 등록')
    print('3. 강의 수정')
    print('4. 강의 삭제')
    print('5. 나가기')
    print('**********************************************************************')


def print_timetable(year, semester):
    '''시간표 출력

    Args:
        year: 학년도 int
        semester: 학기 int
    '''

    target = _timetable[year][semester]
    if not len(target) > 0:
        print('해당 시기의 시간표에 등록된 강의가 없습니다.')
        return

    timetable = convert_timetable(target)

    print_timetable_in_range_time(timetable, 0, 6)
    print_timetable_in_range_time(timetable, 6.5, 12.5)


def select_year_semester():
    '''학년도, 학기 선택

    Returns:
        학년도, 학기
    '''
    year = str(input_range(ljust_consider_kor(YEAR, 10) + '> ',
                           2000, 3000, '올바른 년도를 입력해주세요.'))
    semester = str(input_range(ljust_consider_kor(SEMESTER, 10) + '> ',
                               1, 2, '올바른 학기를 입력해주세요.'))
    return year, semester


def convert_timetable(timetable):
    '''[{요일, 강의실, 강의시간, 강의코드}]의 형태를 {요일: {강의실: {강의시간: 강의코드}}}의 형태로 변환

    출력이나 시간표 등록 시 같은 강의실, 시간에 등록하는 걸 방지하기 위한 비교를 편하게 해줌

    Returns:
        변환된 시간표 dict를 반환
    '''
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
    '''시간표 분할 출력

    한 번에 시간표를 모두 출력하면 너무 길어 콘솔창에서 줄바꿈이 일어나 분할해서 출력

    Args:
        timetable: 시간표 dict
        start: 시작 교시 double
        end: 끝 교시 double
    '''
    cnt = 0
    start_index = (int)(start * 2)
    end_index = (int)(end * 2 + 1)
    boundary_time = TIMES[start_index:end_index]
    print(center_consider_kor('시간', 20), end=' |')
    for time in boundary_time:
        print(center_consider_kor(time, 10), end='|')
    print()

    print(center_consider_kor('요일', 10) + '|' +
          center_consider_kor('강의실', 10) + '|' +
          (center_consider_kor('', 10) + '|') * len(boundary_time))
    lecture_code = None
    prev_lecture = None
    for day in timetable:
        print('-' * len(boundary_time) * 13)
        print(center_consider_kor(day, 10), end='|')
        for room in timetable[day]:
            print(center_consider_kor(room, 10), end='|')
            for index, time in enumerate(boundary_time):
                if lecture_code is not None:
                    prev_lecture = lecture_code
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
                    lecture_code = timetable[day][room][TIMES[index + start_index]]
                    if cnt != 0:
                        if lecture_code is not prev_lecture:
                            lecture_info = get_lecture_info(
                                prev_lecture, cnt)
                            print(
                                center_consider_kor(
                                    lecture_info, 10 * cnt + cnt - 1),
                                end='|'
                            )
                            cnt = 0
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
            if room != list(timetable[day].keys())[-1]:
                print()
                print(center_consider_kor('', 10), end='|')
        print()
    print('-' * len(boundary_time) * 13)
    print()


def get_lecture_info(lecture_code, space):
    '''강의 정보 반환

    강의명(교원명)의 형태로 변환해서 강의 정보 추출.
    넓이가 좁은 경우에는 더 축약해서 반환.

    Args:
        lecture_code: str 강의 코드
        space: int 시간표 내에서 사용 가능 넓이

    Returns:
        강의명(교원명)
    '''
    subject_code = _lectures[lecture_code][SUBJECT_CODE]
    for subject in _subjects:
        if subject[SUBJECT_CODE] == subject_code:
            subject_name = subject[SUBJECT_NAME]
    teacher_name = _lectures[lecture_code][TEACHER]
    if space <= 2:
        return '{0}({1})'.format(subject_name[0:space*3], teacher_name[0:1])
    return '{0}({1})'.format(subject_name[0:space*5], teacher_name[0:3])


def input_timetable(year, semester):
    '''강의 등록

    시간표 내에 강의 등록.
    같은 강의실 같은 시간에 등록하지 못하도록 함.

    Args:
        year: str 강의 코드
        semester: int 시간표 내에서 사용 가능 넓이

    Returns:
        시간표에 입력될 강의 dict
        { 요일, 강의실, 강의, 시간 }
    '''
    if not year in _timetable:
        _timetable[year] = {}
    if not semester in _timetable[year]:
        _timetable[year][semester] = []

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
    return {
        TIMETABLE_DAY: day,
        TIMETABLE_TIME: times,
        TIMETABLE_ROOM: room_code,
        TIMETABLE_LECTURE: lecture_code
    }


def input_room_code():
    '''강의실 코드 입력

    입력한 강의실 코드가 _rooms에 존재하는지 확인 후 반환.
    없으면 재입력.

    Returns:
        강의실 코드
    '''
    while True:
        room_code = input(ljust_consider_kor('강의실 코드', 15) + '> ')

        for room in _rooms:
            if room[ROOM_CODE] == room_code:
                return room_code

        print('해당하는 강의실이 없습니다.')


def input_time():
    '''강의 시간 입력

    '요일/시작시간~끝시간'의 형태로 강의 요일과 시간을 입력.
    형식 오류 시 재입력.

    Returns:
        강의 요일, 강의 시간(09:00~11:00)
    '''
    while True:
        day_times = input('강의 요일/시간 (ex.월요일/09:00~11:00) > ')
        day, times = day_times.split('/')
        if not day in DAYS:
            break
        start, end = times.split('~')
        if not start in TIMES or not end in TIMES:
            break
        if TIMES.index(start) >= TIMES.index(end):
            break
        return day, times

    print('잘못 입력하셨습니다.')
    print('요일/시작시간~종료시간 (ex.월요일/09:00~11:00)의 형태로 입력해주세요.')
    return input_time()


def input_lecture_code():
    '''강의 코드 입력

    입력한 강의실 코드가 _lectures에 존재하는지 확인 후 반환.
    없으면 재입력.

    Returns:
        강의 코드
    '''
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
    if _timetable[year] == None:
        print('강의가 등록된 시간표가 없습니다.')
        return
    if _timetable[year][semester] == None:
        print('강의가 등록된 시간표가 없습니다.')
        return
    target = _timetable[year][semester]
    delindex = select_timetable(target)

    del target[delindex]
    print('해당 강의가 삭제되었습니다.')


def select_timetable(target):
    retrieve_timetable(target)
    print()
    index = input_range("강의 번호 입력 >", 1, len(target), '존재하지 않는 강의 번호입니다.')
    return index - 1


def retrieve_timetable(target):
    print()

    print('등록된 강의 정보')

    for index, target in enumerate(target):
        print('-------------------- -------------------- -------------------- -------------------- --------------------')
        print(
            ljust_consider_kor(str(index + 1), 20),
            ljust_consider_kor(target[TIMETABLE_DAY], 20),
            ljust_consider_kor(target[TIMETABLE_ROOM], 20),
            ljust_consider_kor(target[TIMETABLE_TIME], 20),
            ljust_consider_kor(target[TIMETABLE_LECTURE], 20)
        )
