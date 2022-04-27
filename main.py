from utils import *


def main():
    value = 0
    while value != 7:
        printMenu()
        value = input_number('> ', '1 ~ 6 사이의 수를 입력해주세요.')
        if value == 1:
            print()
        elif value == 2:
            print()
        elif value == 3:
            print()
        elif value == 4:
            print()
        elif value == 5:
            print()
        elif value == 6:
            print()
            print('프로그램을 종료합니다.')
        else:
            print('1 ~ 6 사이의 수를 입력해주세요.')


def printMenu():
    print()
    print('**********************************************************************')
    print('1. 교과목 관리')
    print('2. 강의 관리')
    print('3. 강의실 관리')
    print('4. 시간표 관리')
    print('5. 데이터 관리')
    print('6. 종료')
    print('**********************************************************************')


main()
