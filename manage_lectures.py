from posixpath import split
from utils import *
from constants import *


def manage_lectures(lectures={}, subjects=[]):
    '''강의 관리

    Args:
        lectures: 강의 dict
        subjects: 교과목 array
    '''
    global _subjects
    global _lectures
    _subjects = subjects
    _lectures = lectures

    value = 0
    while value != 5:
        print_menu()
        value = input_number('> ', '1 ~ 5 사이의 수를 입력해주세요.')
        if value == 1:
            print_lectures()
        elif value == 2:
            code, new_lecture = input_lecture()
            _lectures[code] = new_lecture
        elif value == 3:
            code, updated_lecture = update_lecture()
            _lectures[code] = updated_lecture
        elif value == 4:
            _lectures = delete_lecture()
        elif value == 5:
            break
        else:
            print('1 ~ 5 사이의 수를 입력해주세요.')


def print_menu():
    '''강의 메뉴 출력
    '''
    print()
    print('**********************************************************************')
    print('1. 강의 목록 출력')
    print('2. 강의 등록')
    print('3. 강의 수정')
    print('4. 강의 삭제')
    print('5. 나가기')
    print('**********************************************************************')


def print_lectures():
    '''강의 목록 출력

    전체 강의 목록을 출력.
    '''
    print()
    if not len(_lectures) > 0:
        print('등록된 강의가 없습니다.')
        return

    print(
        ljust_consider_kor('No.', 5),
        ljust_consider_kor(LECTURE_CODE, 15),
        ljust_consider_kor('교과목 코드', 15),
        ljust_consider_kor(YEAR, 15),
        ljust_consider_kor(SEMESTER, 15),
        ljust_consider_kor(TEACHER, 15)
    )
    print('-' * 150)

    for index, code in enumerate(_lectures.keys()):
        print(
            ljust_consider_kor(str(index + 1), 5),
            ljust_consider_kor(code[0:15], 15),
            ljust_consider_kor(_lectures[code][SUBJECT_CODE][0:15], 15),
            ljust_consider_kor(_lectures[code][YEAR], 15),
            ljust_consider_kor(_lectures[code][SEMESTER], 15),
            ljust_consider_kor(_lectures[code][TEACHER][0:15], 15)
        )


def input_lecture():
    '''강의 입력

    강의코드, 학년도, 학기, 교원명을 입력 받음.

    Returns:
        강의코드, {교과목코드, 학년도, 학기, 교원명}
    '''
    print()
    code, subject_code = input_code()
    year = str(input_range(ljust_consider_kor(YEAR, 15) + '> ',
                           2000, 3000, '올바른 년도를 입력해주세요.'))
    semester = str(input_range(ljust_consider_kor(SEMESTER, 15) + '> ',
                               1, 2, '올바른 학기를 입력해주세요.'))
    teacher = input(ljust_consider_kor(TEACHER, 15) + '> ')

    return code, {
        SUBJECT_CODE: subject_code,
        YEAR: year,
        SEMESTER: semester,
        TEACHER: teacher
    }


def input_code():
    '''강의 코드 입력

    '교과목코드-분반'의 형태로 입력.
    교과목코드가 _subjects에 존재하지 않으면 재입력.

    Returns:
        강의 코드
    '''
    while True:
        code = input(ljust_consider_kor(
            '강의 코드(MME2051-01)', 15) + '> ')
        subject_code, _ = code.split('-')

        for subject in _subjects:
            if subject[SUBJECT_CODE] == subject_code:
                return code, subject_code

        print('해당하는 교과목이 없습니다.')


def update_lecture():
    '''강의 수정

    Returns:
        수정된 강의
        강의코드, {교과목코드, 학년도, 학기, 교원명}
    '''
    print()
    if not len(_lectures) > 0:
        print('등록된 강의가 없습니다.')
        return
    code = select_lecture()
    del _lectures[code]
    return input_lecture()


def delete_lecture():
    '''강의 삭제
    '''
    print()
    if not len(_lectures) > 0:
        print('등록된 강의가 없습니다.')
        return
    code = select_lecture()
    del _lectures[code]


def select_lecture():
    '''강의 선택

    강의 수정, 삭제 시 대상 강의를 선택.
    강의 목록 출력 후 index를 통해 선택.

    Returns:
        선택된 강의 코드
    '''
    if not len(_lectures) > 0:
        print('등록된 강의가 없습니다.')
        return
    print_lectures()
    print()

    index = input_range('No. > ', 1, len(_lectures), '범위 내의 값을 입력해주세요.') - 1
    selected_code = list(_lectures.keys())[index]
    print_lecture(selected_code)

    return selected_code


def print_lecture(code):
    '''강의 출력

    강의 선택 시 선택된 강의 하나의 정보를 출력
    '''
    print()
    print(ljust_consider_kor(LECTURE_CODE, 15), ':', code)
    print(ljust_consider_kor('교과목 코드', 15), ':', _lectures[code][SUBJECT_CODE])
    print(ljust_consider_kor(YEAR, 15), ':', _lectures[code][YEAR])
    print(ljust_consider_kor(SEMESTER, 15), ':', _lectures[code][SEMESTER])
    print(ljust_consider_kor(TEACHER, 15), ':', _lectures[code][TEACHER])
