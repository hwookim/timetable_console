from utils import *


ID = '강의 코드'
SUBJECT_ID = '교과목 코드'
YEAR = '개설 년도'
SEMESTER = '개설 학기'
TEACHER = '교원명'


def manage_lectures(lectures=[], subjects=[]):
    data = lectures
    value = 0
    while value != 5:
        print_menu()
        value = input_number('> ', '1 ~ 5 사이의 수를 입력해주세요.')
        if value == 1:
            print_lectures(data)
        elif value == 2:
            id, new_lecture = input_lecture(subjects)
            data[id] = new_lecture
        elif value == 3:
            data = update_lecture(data, subjects)
        elif value == 4:
            data = delete_lecture(data)
        elif value == 5:
            break
        else:
            print('1 ~ 5 사이의 수를 입력해주세요.')

    return data


def print_menu():
    print()
    print('**********************************************************************')
    print('1. 강의 목록 출력')
    print('2. 강의 등록')
    print('3. 강의 수정')
    print('4. 강의 삭제')
    print('5. 나가기')
    print('**********************************************************************')


def print_lectures(lectures=[]):
    print()
    if not len(lectures) > 0:
        print('등록된 강의가 없습니다.')
        return
    print('No.\t\t {0}\t {1}\t {2}\t {3}\t {4}'.format(
        ID, SUBJECT_ID, YEAR, SEMESTER, TEACHER))
    print('-' * 150)
    for index, id in enumerate(lectures.keys()):
        print('%-15d %-15s %-15s %-15d %-15d %-15s' %
              (index + 1, id[0:15], lectures[id][SUBJECT_ID][0:15],
               lectures[id][YEAR], lectures[id][SEMESTER], lectures[id][TEACHER][0:15]))


def input_lecture(subjects=[]):
    print()
    id = input(ljust_consider_kor(ID, 15) + '> ')
    subject_id = input_subject(subjects)
    year = input_range(ljust_consider_kor(YEAR, 15) + '> ',
                       2000, 3000, '올바른 년도를 입력해주세요.')
    semester = input_range(ljust_consider_kor(SEMESTER, 15) + '> ',
                           1, 2, '올바른 학기를 입력해주세요.')
    teacher = input(ljust_consider_kor(TEACHER, 15) + '> ')

    return id, {
        SUBJECT_ID: subject_id,
        YEAR: year,
        SEMESTER: semester,
        TEACHER: teacher
    }


def input_subject(subjects=[]):
    while True:
        subject_id = input(ljust_consider_kor(SUBJECT_ID, 15) + '> ')

        for subject_id in subjects:
            return subject_id

        print('해당하는 교과목이 없습니다.')


def update_lecture(lectures=[], subjects=[]):
    data = lectures

    print()
    if not len(data) > 0:
        print('등록된 강의가 없습니다.')
        return
    id = select_lecture(data)
    data[id] = input_lecture(subjects)

    return data


def delete_lecture(lectures=[]):
    data = lectures

    print()
    if not len(data) > 0:
        print('등록된 강의가 없습니다.')
        return
    id = select_lecture(data)
    del data[id]

    return data


def select_lecture(lectures=[]):
    data = lectures

    if not len(data) > 0:
        print('등록된 강의가 없습니다.')
        return
    print_lectures(data)
    print()

    index = input_range('No. > ', 1, len(data), '범위 내의 값을 입력해주세요.') - 1
    selected_id = list(lectures.keys())[index]
    print_lecture(lectures, selected_id)

    return selected_id


def print_lecture(lectures, id):
    print()
    print(ljust_consider_kor(ID, 15) + ': %s' % id)
    print(ljust_consider_kor(SUBJECT_ID, 15) +
          ': %s' % lectures[id][SUBJECT_ID])
    print(ljust_consider_kor(YEAR, 15) + ': %d' % lectures[id][YEAR])
    print(ljust_consider_kor(SEMESTER, 15) + ': %d' % lectures[id][SEMESTER])
    print(ljust_consider_kor(TEACHER, 15) + ': %s' % lectures[id][TEACHER])


# manage_lectures({}, {'MME': 'h'})
