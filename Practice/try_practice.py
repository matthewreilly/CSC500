
def get_user_nums():
    user_nums = []
    valid_input = False
    while valid_input == False:
        try:
            num1 = int(input('Enter an integer:\n'))
            user_nums.append(num1)
        except ValueError:
            print('Invalid input')
            continue
        valid_input = True

    valid_input = False
    while valid_input == False:
        try:
            num2 = float(input('Enter a float:\n'))
            user_nums.append(num2)
        except ValueError:
            print('Invalid input')
            continue
        valid_input = True
    return user_nums


if __name__ == '__main__':
    user_nums = get_user_nums()
    print('User_nums: {}'.format(user_nums))
