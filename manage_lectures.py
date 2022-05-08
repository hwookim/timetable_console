from utils import *
from constants import *


def manage_lectures(lectures=[], subjects=[]):
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
            id, new_lecture = input_lecture()
            _lectures[id] = new_lecture
        elif value == 3:
            id, updated_lecture = update_lecture()
            _lectures[id] = updated_lecture
        elif value == 4:
            _lectures = delete_lecture()
        elif value == 5:
            break
        else:
            print('1 ~ 5 사이의 수를 입력해주세요.')


def print_menu():
    print()
    print('**********************************************************************')
    print('1. 강의 목록 출력')
    print('2. 강의 등록')
    print('3. 강의 수정')
    print('4. 강의 삭제')
    print('5. 나가기')
    print('**********************************************************************')


def print_lectures():
    print()
    if not len(_lectures) > 0:
        print('_등록된 강의가 없습니다.')
        return

    print(
        ljust_consider_kor('No.', 5),
        ljust_consider_kor(LECTURE_ID, 15),
        ljust_consider_kor('교과목 코드', 15),
        ljust_consider_kor(YEAR, 15),
        ljust_consider_kor(SEMESTER, 15),
        ljust_consider_kor(TEACHER, 15)
    )
    print('-' * 150)

    for index, id in enumerate(_lectures.keys()):
        print(
            ljust_consider_kor(str(index + 1), 5),
            ljust_consider_kor(id[0:15], 15),
            ljust_consider_kor(_lectures[id][SUBJECT_ID][0:15], 15),
            ljust_consider_kor(_lectures[id][YEAR], 15),
            ljust_consider_kor(_lectures[id][SEMESTER], 15),
            ljust_consider_kor(_lectures[id][TEACHER][0:15], 15)
        )


def input_lecture():
    print()
    id = input(ljust_consider_kor(LECTURE_ID, 15) + '> ')
    subject_id = input_subject()
    year = str(input_range(ljust_consider_kor(YEAR, 15) + '> ',
                           2000, 3000, '올바른 년도를 입력해주세요.'))
    semester = str(input_range(ljust_consider_kor(SEMESTER, 15) + '> ',
                               1, 2, '올바른 학기를 입력해주세요.'))
    teacher = input(ljust_consider_kor(TEACHER, 15) + '> ')

    return id, {
        SUBJECT_ID: subject_id,
        YEAR: year,
        SEMESTER: semester,
        TEACHER: teacher
    }


def input_subject():
    while True:
        subject_id = input(ljust_consider_kor('교과목 코드', 15) + '> ')

        for subject in _subjects:
            if subject[SUBJECT_ID] == subject_id:
                return subject_id

        print('해당하는 교과목이 없습니다.')


def update_lecture():
    print()
    if not len(_lectures) > 0:
        print('등록된 강의가 없습니다.')
        return
    id = select_lecture()
    del _lectures[id]
    return input_lecture()


def delete_lecture():
    print()
    if not len(_lectures) > 0:
        print('등록된 강의가 없습니다.')
        return
    id = select_lecture()
    del _lectures[id]

    return _lectures


def select_lecture():
    if not len(_lectures) > 0:
        print('등록된 강의가 없습니다.')
        return
    print_lectures()
    print()

    index = input_range('No. > ', 1, len(_lectures), '범위 내의 값을 입력해주세요.') - 1
    selected_id = list(_lectures.keys())[index]
    print_lecture(selected_id)

    return selected_id


def print_lecture(id):
    print()
    print(ljust_consider_kor(LECTURE_ID, 15), ':', id)
    print(ljust_consider_kor('교과목 코드', 15), ':', _lectures[id][SUBJECT_ID])
    print(ljust_consider_kor(YEAR, 15), ':', _lectures[id][YEAR])
    print(ljust_consider_kor(SEMESTER, 15), ':', _lectures[id][SEMESTER])
    print(ljust_consider_kor(TEACHER, 15), ':', _lectures[id][TEACHER])
