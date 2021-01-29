# CSC 500, Module 6 Critical Thinking - Option #1
# Created by Matt Reilly. 19 Jan 2021

# References:
# Lysecky, et al. (2019). CSC500: principles of programming. zyBooks.
#   https://learn.zybooks.com/zybook/CSC500zyBookInteractiveText2020
# Reading and Writing to text files in Python. (2017, April 3). Geeks for Geeks.
#   https://www.geeksforgeeks.org/reading-writing-text-files-python/
#//////////////////////////////////////////////////////////////////////////////
def display_instructions():
    print('\nThis program reads student test answers from a text file.')
    print('It then compares these answers to an answer key and returns the\n\
number of correct and incorrect answers and a list of the quetions missed.\n')
    return
#//////////////////////////////////////////////////////////////////////////////
# Open text file w/ student answers
# Move these answers into a list for later comparison to the answer key
def load_student_answers(student_answer_file):
    student_answer_file = open(student_answer_file)
    student_answers = student_answer_file.readlines()
    student_answer_file.close()
    return student_answers
#//////////////////////////////////////////////////////////////////////////////
# Compare student's answers vs the answer key
def compare_answers(answer_key, student_answers):
    num_wrong = 0
    list_wrong = []

    for i in range(len(answer_key)):
        if answer_key[i] not in student_answers[i]:
            num_wrong += 1
            list_wrong.append(i+1)

    num_correct = len(answer_key) - num_wrong

    return num_correct, num_wrong, list_wrong
#//////////////////////////////////////////////////////////////////////////////
# Determine if the student passes. Passing requires 15 correct answers out of 20
#   (75%). I went w/ a percentage (rather than checking for 15 correct answers)
#   so the program is more easily adaptable to grading tests w/ more or fewer
#   than 20 questions.
def display_results(num_correct, num_wrong, list_wrong):
    passing_percentage = .75
    if num_correct / len(answer_key) >= .75:
        print('Congratulations! You passed.')

    print('You answered {} questions correctly and {} incorrectly.\n'.format(num_correct, num_wrong))
    print('You missed the following questions:\n')
    print(list_wrong)
    return
#//////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    display_instructions()
    student_answer_file = 'student_answers.txt'
    student_answers = load_student_answers(student_answer_file)
    answer_key = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C',\
    'B','B','D','A']
    num_correct, num_wrong, list_wrong = compare_answers(answer_key, student_answers)
    display_results(num_correct, num_wrong, list_wrong)
