from typing import List

from tabulate import tabulate


def test1():
    cat_dog_duck: List[str] = ['cat', 'dog', 'duck']
    my_list = cat_dog_duck

    for elem in my_list[:]:
        if len(elem) > 3:
            print(elem)
            my_list.append(elem)

    print(my_list)


def test2():
    print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age']))


def test3():
    """
    It's a test doc
    """
    table_columns = []
    user_answer = ''
    menu = "Введите через запятую имя и возраст. " \
           "Если хотите закончить, введите 'end'\n"
    while user_answer != 'end':
        user_answer = input(menu)
        if user_answer == 'end':
            print('Exit from the app')
            break
        else:
            ans_words = user_answer.replace(' ', '').split(',')

            if len(ans_words) == 2:
                try:
                    ans_words[1] = int(ans_words[1])
                except ValueError:
                    print('Second arg do not int')

                except IndexError:
                    print('Just one arg')

                if isinstance(ans_words[1], int):
                    table_columns.append(ans_words)

            else:
                print('Don\'t recognized format')

    print(
        tabulate(
            table_columns,
            headers=['Name', 'Age'],
            showindex="always")
    )


test3()
