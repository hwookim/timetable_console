from utils import *

def manageSubjects(subjects=[]):
    global manageSubject
    manageSubject = subjects
    value = 0
    while value != 7:
        printMenu()
        value = inputNumber('> ', 'Input 1 ~ 7!')
        if value == 1:
            retrieveSubject()
        elif value == 2:
            manageSubject.append(inputSubject())
        elif value == 3:
            updateSubject()
        elif value == 4:
            deleteSubject()
        elif value == 5:
            print()
            print('Bye!!')
            break
        else:
            print('Input 1 ~ 5!')


def inputNumber(message: str, error: str):
    try:
        value = int(input(message))
        return value
    except ValueError:
        print(error)
        return inputNumber(message, error)


def printMenu():
    print()
    print('**********************************************************************')
    print(' 1. Retrieve')
    print(' 2. Input')
    print(' 3. Update')
    print(' 4. Delete')
    print(' 5. Quit')
    print('**********************************************************************')


def retrieveSubject():
    print()

    if len(manageSubject) == 0:
        print('There is no data.')
        return

    print('입력된 교과목 정보')
    for index, subject in enumerate(manageSubject):
        print('-------------------- -------------------- -------------------- -------------------- -------------------- --------------------')
        print(
                ljust_consider_kor(str(index + 1), 20),
                ljust_consider_kor(subject['subjectCode'], 20),
                ljust_consider_kor(subject['subjectName'], 20),
                ljust_consider_kor(subject['subjectGrade'], 20),
                ljust_consider_kor(subject['subjectSem'], 20),
                ljust_consider_kor(subject['subjectEx'], 20),
            )


def inputSubject():
    print()
    subjectCode = input('교과목 코드    >')
    subjectName = input('교과목 명칭    >')
    subjectGrade = input('학년           >')
    subjectSem = input('학기           >')
    subjectEx = input('교과목 해설    >')

    return {'subjectCode': subjectCode, 'subjectName': subjectName, 'subjectGrade': subjectGrade, 'subjectSem': subjectSem, 'subjectEx': subjectEx}


def updateSubject():
    index = selectSubject()
    manageSubject[index] = inputSubject()

    print()
    print('Updated.')
    retrieveSubject()


def deleteSubject():
    index = selectSubject()
    del manageSubject[index]

    print()
    print('Deleted.')
    retrieveSubject()


def printGrade(index: int):
    manageSubjects = manageSubject[index]
    print('교과목 코드      :%s' % manageSubjects['subjectCode'])
    print('교과목 명칭      :%s' % manageSubjects['subjectName'])
    print('학년             :%s' % manageSubjects['subjectGrade'])
    print('학기             :%s' % manageSubjects['subjectSem'])
    print('교과목 해설      :%s' % manageSubjects['subjectEx'])


def selectSubject():
    retrieveSubject()
    print()
    index = inputRange('index> ', 1, len(manageSubject)) - 1
    printGrade(index)

    return index


def inputRange(message: str, start: int, end: int):
    value = start - 1
    error = f'Please enter a number between {start} to {end}!!'
    while value < start or value > end:
        value = inputNumber(message, error)
        if value >= start and value <= end:
            break
        print(error)

    return value
