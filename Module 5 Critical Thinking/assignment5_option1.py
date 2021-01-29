# CSC 500, Module 5 Critical Thinking - Option #1
# Created by Matt Reilly. 18 Jan 2021

# References:
# Lysecky, et al. (2019). CSC500: principles of programming. zyBooks.
#   https://learn.zybooks.com/zybook/CSC500zyBookInteractiveText2020
# Python Strings. (2020, January 10). ThePythonGuru. https://thepythonguru.com/python-strings
#//////////////////////////////////////////////////////////////////////////////
# Explain program to user
def display_instructions():
    print('\nThis program allows you to enter two primary colors and outputs \
the resulting secondary color.')
    print('The primary colors are red, blue, and yellow.')
    return
#//////////////////////////////////////////////////////////////////////////////
# Prompt user to enter 2 primary colors. Display error message and reprompt for
#   input if user enters a non-primary color or if user enters the same color
#   twice. No point in mixing two of the same color...

def get_colors():
    # Using a while loop  and "if" statements to enable reprompting if user
    #   enters an invalid input (non-primary color or same color twice).
    valid_color1 = False
    while valid_color1 == False:
        color1 = input('Enter the first primary color:\n')
        # If user enters a valid primary color, continue to color2.
        if color1 == 'red' or color1 == 'blue' or color1 == 'yellow':
            valid_color1 = True

        # If user doesn't enter a primary color, display error message and
        #   reprompt for input
        else:
            print('Invalid input. Please try again.\n')
            continue

    valid_color2 = False
    while valid_color2 == False:
        color2 = input('Enter the second primary color:\n')

        if color2 == 'red' or color2 == 'blue' or color2 == 'yellow':
            if color2 == color1: # no point mixing two of the same color...
                print('You already entered {}. Select a different primary \
color.\n'.format(color2))
                continue
            else:
                valid_color2 = True
        else:
            print('Invalid input. Please try again.\n')
            continue

    return color1, color2
#//////////////////////////////////////////////////////////////////////////////
def mix_colors(color1, color2):
    # Red + blue = purple
    if (color1=='red' or color2=='red') and (color1=='blue' or color2=='blue'):
        final_color = 'purple'

    # Red + yellow = orange
    if (color1=='red' or color2=='red') and (color1=='yellow' or color2=='yellow'):
        final_color = 'orange'

    # Blue + yellow = green
    if (color1=='blue' or color2=='blue') and (color1=='yellow' or color2=='yellow'):
        final_color = 'green'

    return final_color
#//////////////////////////////////////////////////////////////////////////////
def display_results(color1, color2, final_color):
    print('{} and {} combine to make {}'.format(color1, color2, final_color))
    return
#//////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    display_instructions()
    color1, color2 = get_colors()
    final_color = mix_colors(color1, color2)
    display_results(color1, color2, final_color)
