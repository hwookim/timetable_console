from utils import *


TIMES = ('08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
         '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:25', '18:50', '19:15', '19:40', '20:05')

DAYS = ('월요일', '화요일', '수요일', '목요일', '금요일')


def manage_timetable(timetable=[], lectures=[], rooms=[]):
    data = timetable
    value = 0
    while value != 5:
        print_menu()
        value = input_number('> ', '1 ~ 4 사이의 수를 입력해주세요.')
        if value == 1:
            print_timetable(timetable, lectures)
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


def print_timetable(timetable=[], lectures=[]):
    print()
    if not len(timetable) > 0:
        print('시간표에 등록된 강의가 없습니다.')
        return

    print_timetable_in_range_time(timetable, lectures, 0, 6)
    print_timetable_in_range_time(timetable, lectures, 6.5, 12.5)


def print_timetable_in_range_time(timetable=[], lectures=[], start=0, end=6):
    cnt = 0
    boundaryTime = TIMES[(int)(start * 2):(int)(end * 2 + 1)]
    print(center_consider_kor('시간', 20), end=' |')
    for time in boundaryTime:
        print(center_consider_kor(time, 10), end='|')
    print()

    print(center_consider_kor('요일', 10) + '|' + center_consider_kor('강의실', 10))
    for day in timetable:
        print('-' * 175)
        print(center_consider_kor(day, 10), end='|')
        for room in timetable[day]:
            print(center_consider_kor(room, 10), end='|')
            for index, time in enumerate(boundaryTime):
                if not time in timetable[day][room]:
                    if cnt != 0:
                        lectureCode = timetable[day][room][TIMES[index - 1]]
                        lectureInfo = get_lecture_info(lectureCode, lectures)
                        print(
                            center_consider_kor(
                                lectureInfo, 10 * cnt + cnt - 1),
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


def get_lecture_info(lectureCode, lectures):
    return '{0}({1})'.format(
        lectures[lectureCode]['강의명'][0:10], lectures[lectureCode]['교원명']
    )


'''
실행 예시
- 데이터 변경 필요
'''
print_timetable(
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
    {'MME-01': {'강의명': '자율사물기초프로그래밍', '교원명': '성연식'}}
)
