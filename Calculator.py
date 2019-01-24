# Text displayed to user
first_question_text: str = '''
    What are you want to do?
    1. +
    2. -
    3. *
    4. 
'''

first_question_text = first_question_text.strip('\n')

# Answer options available to user
first_answer_options = ([1, '+'], [2, '-'], [3, '*'], [4, '/'])
final_answer_options = {'fire', 'do', 'end', '='}
positive_answer_options = {'yes', 'y', 'yeah', 'yap', 'positive', '+'}
negative_answer_options = {'no', 'n', 'nope', 'ne', 'negative', '-'}


def first_answer_input_check(answer=''):
    # TODO: add more tests for user answer
    if len(answer) == 0:
        return [1, 'there is no answer']
    else:
        return [0, '']

# first_question_answer: str = input(first_question_text)
#
# first_answer_test_code, first_answer_test_comment = \
#     first_answer_input_check(answer=first_question_answer)
#
# first_message_to_user = ''
#
# if first_answer_test_code == 0:
#     first_message_to_user = 'Your choice is ' + \
#                             first_question_answer + \
#                             '. Is that right?\n'
# else:
#     if first_answer_test_code != 1:
#         first_message_to_user = 'Your answer is' + \
#                                 first_question_answer + \
#                                 '. '
#     if first_answer_test_code > 0:
#         first_message_to_user = 'Sorry, but ' + \
#                                 first_answer_test_comment + \
#                                 '.\n'
#
# print(first_message_to_user)
