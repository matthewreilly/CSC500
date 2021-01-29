# This program prompts the user to enter two numbers and outputs the sum and
# difference (num1 - num2) of the two numbers. The program will continue to
# re-prompt the user for numerical inputs if a non-number is entered. The
# program will accept decimals and commas within the numbers, but will not
# accept scientific notation. Answers will be didsplayed with 2 decimal places.
#
#/////////////////////////////////////////////////////////////////////////////
def display_instructions():
    print('Enter two numbers to find their sum and difference (1st number - \
second number).')
    print('The numbers may contain commas and a decimal point.')
    print('This program will not accept numbers in scientific notation.')
    return
#/////////////////////////////////////////////////////////////////////////////
def get_numbers():
    chars1 = ''
    chars2 = ''
    # Run this loop until user provides two valid numerical inputs
    while (chars1.isnumeric() == False) or (chars2.isnumeric() == False):
        num1 = input('Enter the first number: ').replace(',','')
        num2 = input('Enter the second number: ').replace(',','')
        chars1 = num1.replace('.','') # Remove decimal points if necessary
        chars2 = num2.replace('.','')
        # If user didn't enter 2 numbers (excluding commas and decimal points)
        if (chars1.isnumeric() == False) or (chars2.isnumeric() == False):
            print("Entries must be numeric. Please try again.")
    return float(num1), float(num2)
#/////////////////////////////////////////////////////////////////////////////
def do_math(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    return sum, difference
#/////////////////////////////////////////////////////////////////////////////
def display_answers(sum, difference):
    print("The sum of {} and {} is {:.2f}".format(num1, num2, sum))
    print("{} minus {} equals {:.2f}".format(num1, num2, difference))
    return
#/////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    display_instructions()
    num1, num2 = get_numbers()
    sum, difference = do_math(num1, num2)
    display_answers(sum, difference)
