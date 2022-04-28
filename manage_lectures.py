from numpy import delete
from utils import *


def manage_lectures(lectures=[]):
    data = lectures
    value = 0
    while value != 5:
        print_menu()
        value = input_number('> ', '1 ~ 5 사이의 수를 입력해주세요.')
        if value == 1:
            print_lectures(data)
        elif value == 2:
            data.append(input_lecture())
        elif value == 3:
            data = update_lecture(data)
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
    if not len(lectures) > 0:
        print('등록된 강의가 없습니다.')
        return
    print('No.\t\t 강의 코드\t 교과목 코드\t 개설 학년\t 개설 학기\t 교원명')
    print('--------------- --------------- --------------- --------------- --------------- ---------------\t')
    for index, lecture in enumerate(lectures):
        print('%-15d %-15s %-15s %-15d %-15d %-15s' %
              (index + 1, lecture['id'][0:15], lecture['subject_id'][0:15],
               lecture['year'], lecture['semester'], lecture['teacher'][0:15]))


def input_lecture():
    print()
    id = input('강의 코드\t > ')
    subject_id = input('교과목 코드\t > ')
    year = input_range('개설 년도\t > ', 2000, 3000, '올바른 년도를 입력해주세요.')
    semester = input_range('개설 학기\t > ', 1, 2, '올바른 학기를 입력해주세요.')
    teacher = input('교원명\t\t > ')

    return {'id': id, 'subject_id': subject_id,
            'year': year, 'semester': semester,
            'teacher': teacher}


def update_lecture(lectures=[]):
    data = lectures

    print()
    if not len(data) > 0:
        print('등록된 강의가 없습니다.')
        return
    index = select_lecture(data)
    data[index] = input_lecture()

    return data


def delete_lecture(lectures=[]):
    data = lectures

    print()
    if not len(data) > 0:
        print('등록된 강의가 없습니다.')
        return
    index = select_lecture(data)
    del data[index]

    return data


def select_lecture(lectures=[]):
    data = lectures

    if not len(data) > 0:
        print('등록된 강의가 없습니다.')
        return
    print_lectures(data)
    print()

    index = input_range('No. > ', 1, len(data), '범위 내의 값을 입력해주세요.') - 1
    print_lecture(data[index])

    return index


def print_lecture(lecture):
    print()
    print('강의 코드\t : %s' % lecture['id'])
    print('교과목 코드\t : %s' % lecture['subject_id'])
    print('개설 학년\t : %d' % lecture['year'])
    print('개설 학기\t : %d' % lecture['semester'])
    print('교원명\t\t : %s' % lecture['teacher'])
