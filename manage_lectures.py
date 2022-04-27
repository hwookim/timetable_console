from numpy import delete
from utils import *


def manage_lectures(lectures=[]):
    value = 0
    while value != 5:
        print_menu()
        value = input_number('> ', '1 ~ 5 사이의 수를 입력해주세요.')
        if value == 1:
            print_lectures(lectures)
        elif value == 2:
            lectures.append(input_lecture())
        elif value == 3:
            update_lecture()
        elif value == 4:
            delete_lecture()
        elif value == 5:
            break
        else:
            print('1 ~ 5 사이의 수를 입력해주세요.')

    return lectures


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


def update_lecture():
    print()


def delete_lecture():
    print()


manage_lectures()
