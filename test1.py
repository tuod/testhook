from tabulate import tabulate


def test1():
    myList = ['cat', 'dog', 'duck']

    for elem in myList[:]:
        if len(elem) > 3:
            print(elem)
            myList.append(elem)

    print(myList)


def test2():
    print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age']))


def test3():
    columns = []
    ans = ''
    menu = "Введите через запятую имя и возраст. Если хотите закончить, введите 'end'\n"
    while ans != 'end':
        ans = input(menu)
        if ans == 'end':
            print('Exit from the app')
            break
        else:
            ans_words = ans.replace(' ', '').split(',')

            if len(ans_words) == 2:
                try:
                    ans_words[1] = int(ans_words[1])
                except ValueError:
                    print('Second arg do not int')

                except IndexError:
                    print('Just one arg')

                if isinstance(ans_words[1], int):
                    columns.append(ans_words)

            else:
                    print('Don\'t recognized format')

    print(tabulate(columns, headers=['Name', 'Age']))


def test4():
    pass


test3()
