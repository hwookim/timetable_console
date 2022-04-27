import pickle

grades = []


def main():
    value = 0
    while value != 7:
        printMenu()
        value = inputNumber('> ', 'Input 1 ~ 7!')
        if value == 1:
            retrieveGrades()
        elif value == 2:
            grades.append(inputGrade())
        elif value == 3:
            updateGrade()
        elif value == 4:
            deleteGrade()
        elif value == 5:
            saveGrades()
        elif value == 6:
            loadGrades()
        elif value == 7:
            print()
            print('Bye!!')
        else:
            print('Input 1 ~ 7!')


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
    print(' 5. Save')
    print(' 6. Load')
    print(' 7. Quit')
    print('**********************************************************************')


def retrieveGrades():
    print()

    if len(grades) == 0:
        print('There is no data.')
        return

    print('Index      ID         Name       Korean     English    Math')
    print('---------- ---------- ---------- ---------- ---------- ----------')
    for index, grade in enumerate(grades):
        print('%-10d %-10s %-10s %10d %10d %10d' % (index + 1, grade['id'],
              grade['name'], grade['korean'], grade['english'], grade['math']))


def inputGrade():
    print()
    id = input('ID      > ').upper().lstrip().rstrip()
    name = input('Name    > ').title().lstrip().rstrip()
    korean = inputRange('Korean  > ', 0, 100)
    english = inputRange('English > ', 0, 100)
    math = inputRange('Math    > ', 0, 100)

    return {'id': id, 'name': name, 'korean': korean,
            'english': english, 'math': math}


def inputRange(message: str, start: int, end: int):
    value = start - 1
    error = f'Please enter a number between {start} to {end}!!'
    while value < start or value > end:
        value = inputNumber(message, error)
        if value >= start and value <= end:
            break
        print(error)

    return value


def updateGrade():
    index = selectGrade()
    grades[index] = inputGrade()

    print()
    print('Updated.')
    retrieveGrades()


def printGrade(index: int):
    grade = grades[index]
    print('ID      :%s' % grade['id'][0][:10])
    print('Name    :%s' % grade['name'][0][:10])
    print('Korean  :%d' % grade['korean'])
    print('English :%d' % grade['english'])
    print('Math    :%d' % grade['math'])


def deleteGrade():
    index = selectGrade()
    del grades[index]

    print()
    print('Deleted.')
    retrieveGrades()


def selectGrade():
    retrieveGrades()
    print()
    index = inputRange('index> ', 1, len(grades)) - 1
    printGrade(index)

    return index


def saveGrades():
    with open('grades.dat', 'wb') as file:
        pickle.dump(grades, file)

    print()
    print('Saved.')


def loadGrades():
    grades.clear()
    with open('grades.dat', 'rb') as file:
        grades.extend(pickle.load(file))

    print()
    print('Loaded.')


main()
