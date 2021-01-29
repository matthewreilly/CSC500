# CSC 500, Module 4 Critical Thinking - Option #1
# Created by Matt Reilly. 18 Jan 2021

# References:
# Lysecky, et al. (2019). CSC500: principles of programming. zyBooks.
#   https://learn.zybooks.com/zybook/CSC500zyBookInteractiveText2020
#//////////////////////////////////////////////////////////////////////////////
# Explain program to user
def display_instructions():
    print('\nThis program calculates the average and total rainfall over a given \
period of time.')
    print('You must enter a number of years (positive whole number).')
    print('Then you must enter the rainfall for each month.')
    print()
#//////////////////////////////////////////////////////////////////////////////
# Prompt user to enter inches of rainfall for a given month.
# If user enters invalid input (a non-number), display error message and
#   reprompt for input.
def get_user_input():
    valid_input = False
    while valid_input == False:
        try:
            in_rain = float(input('Enter inches of rainfall for the month:\n'))
        # If user entry is invalid, reprompt for monthly rainfall input
        except ValueError:
            print('Invalid input. You must enter a number. Try again.\n')
            continue
        valid_input = True
    return in_rain
#//////////////////////////////////////////////////////////////////////////////
# Take the list of monthly rainfalls, and return the number of months (num_months),
#   total rainfall (total_rain), and average rainfall per month (avg_rain)
def do_math(list_rain):
    num_months = len(list_rain)
    total_rain = sum(list_rain)
    avg_rain = float(total_rain / num_months)
    return num_months, total_rain, avg_rain
#//////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    display_instructions()
    valid_input = False
    while valid_input == False:
        try:
            year = int(input('Enter number of years:\n'))
        except ValueError:
            print('Invalid input. Try againn\n')
            continue
        valid_input = True

    list_rain = []
    for i in range(year):
        for x in range(12):
            in_rain = get_user_input()
            list_rain.append(in_rain)

    num_months, total_rain, avg_rain = do_math(list_rain)

    # Display results to user
    print('Months of data:', num_months)
    print('Total rainfall: {:.2f}'.format(total_rain))
    print('Average: {:.2f} inches'.format(avg_rain))
