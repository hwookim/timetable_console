from utils import *


def mainRoom(room=[]):
    global Room
    Room = room
    a = 0
    while a != 5:
        printMenu()
        a = selectMenu()

        if len(Room) == 0 and a != 2:
            if a == 5:
                pass
            else:
                print('\nlist is empty! please input classroom data!\n')
                continue

        if a == 1:
            printRoom()\

        elif a == 2:
            Room.append(inputRoom())\

        elif a == 3:
            updateRoom()

        elif a == 4:
            deleteRoom()

        elif a == 5:
            print('\n끝내기')
            break

        else:
            print('Please enter a number between 1 to 5!!\n')

    return Room


def printMenu():
    print('\n')
    print('*' * 80)
    print('1. 강의실 목록 출력')
    print('2. 강의실 정보 입력')
    print('3. 강의실 정보 수정')
    print('4. 강의실 정보 삭제')
    print('5. 강의실 관리 끝내기')
    print('*' * 80)


def selectMenu():
    while True:
        try:
            menu = int(input('>'))

        except ValueError:
            print('Please enter a number!')
            continue
        break
    return menu


def printRoom():
    print('\n')
    print(ljust_consider_kor('index', 20),
          ljust_consider_kor('강의실 코드', 20),
          ljust_consider_kor('명칭', 20),
          rjust_consider_kor('수용가능인원', 20)
          )
    print(('-' * 20 + ' ') * 4)
    for i, item in enumerate(Room):
        print('{:<20}'.format(i+1),
              ljust_consider_kor(item['Code'], 20),
              ljust_consider_kor(item['Name'], 20),
              rjust_consider_kor(item['Capacity'], 20))
    print('\n')


def inputRoom():
    print('\n')
    Code = input('Code\t>')
    Name = input('Name\t>')
    Capacity = input('Capacity>')
    print('\n')
    return {'Code': Code, 'Name': Name, 'Capacity': Capacity}


def inputIndex():
    while True:
        index = int(input('index>'))

        if 0 >= index or index > len(Room):
            print('Please enter a number between 1 to ', len(Room), '!!', sep='')
            continue

        break
    return index


def deleteRoom():
    printRoom()
    index = inputIndex()
    del Room[index-1]
    print('Deleted!\n')
    return Room


def updateRoom():
    printRoom()
    index = inputIndex()
    del Room[index-1]
    Room.insert(index-1, inputRoom())
    return Room
