# Course: CSC500, Week 3 Critical Thinking Assignment. Option #1: Alarm Time
# Created by Matt Reilly. 16 January 2021

# References:
# Lysecky, et al. (2019). CSC500: principles of programming. zyBooks.
#   https://learn.zybooks.com/zybook/CSC500zyBookInteractiveText2020
#//////////////////////////////////////////////////////////////////////////////
# This program asks the user to enter the current time (in hours using
#   24-hour clock format) and for a number of hours to wait. The program
#   outputs the resulting time (in 24-hour clock format)
import math

def display_instructions():
    print('This program allows you to input the current time and the number of \
hours to wait before sounding your alarm.')
    print('Enter current time in 24-hour clock format.')
    print('You may enter just hours (ex: 15) \
or hours and minutes (ex: 1500, 1831, 0230, etc.).')
    print('Number of hours to wait must be a positive integer.')
    return
#//////////////////////////////////////////////////////////////////////////////
def get_user_input():

    # Prompt user to enter current time in hours, ensure valid input, convert
    #   input string to integer
    valid_time = False
    while valid_time == False:
        minutes = 0
        current_time = input('Please enter the current time: \n')

        # Check for valid input
        if current_time.isnumeric() == False: # If user did not enter a number
            print('That is not a valid time entry. Please try again.\n')
            continue

        if len(current_time) == 4:
            current_time = int(current_time)
            minutes = current_time % 100
            current_time = int(current_time / 100) # reduces current_time to just hours
            current_time = str(current_time)

            if minutes >= 60:
                print('That is not a valid time entry. Please try again.\n')
                continue

        # User entered only hours (i.e. 15 instead of 1500)
        if len(current_time) == 2 or len(current_time) == 1:
            current_time = int(current_time)

            # If that number is in the correct range (0-24 inclusive)
            if (current_time >= 0) & (current_time <= 23):
                valid_time = True

            else: # Input is not between 0-24 inclusive
                print('That is not a valid time entry. Please try again.\n')
                continue
        else: # Input is not between 0-24 inclusive
            print('That is not a valid time entry. Please try again.\n')
            continue

    # Prompt user for number of hours to wait, ensure valid entry, convert
    #   user input string to an int
    valid_wait = False
    while valid_wait == False:
        wait_time = input('Please enter the number of hours you want to wait:\n')

        # If input is valid (input is a positive integer)
        if wait_time.isnumeric() == True:
            wait_time = int(wait_time)
            valid_wait = True
        # Else input is not valid:
        else:
            print('That is not a valid number of hours to wait.')
            print('Please try again.\n')

    return current_time, minutes, wait_time
#//////////////////////////////////////////////////////////////////////////////
def do_math(current_time, minutes, wait_time):
    # Add current_time (in hours) to wait_time (in hours), then subtract by 24
    #   until the result is a number less than 24. This is hour portion of the
    #   final time
    final_hours = current_time + wait_time
    days = math.floor(final_hours / 24)
    final_hours = final_hours - (days * 24)

    if minutes < 10:
        minutes = '0' + str(minutes)

    if final_hours < 10:
        final_time = '0' + str(final_hours) + str(minutes)

    else:
        #final_hours = str(final_hours)
        final_time = str(final_hours) + str(minutes)

    return final_time
#//////////////////////////////////////////////////////////////////////////////
def display_results(final_time):
    print('Your alarm will sound at {} hours'.format(final_time))
    return
#//////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    display_instructions()
    current_time, minutes, wait_time = get_user_input()
    final_time = do_math(current_time, minutes, wait_time)
    display_results(final_time)
