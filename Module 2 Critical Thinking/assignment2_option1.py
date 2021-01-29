# Course: CSC500, Week 2 Critical Thinking, Option #1
# This program prompts the user to enter item prices. Instructions for this
#   assignment specify 5 retail items. However, this program allows for any
#   number of item prices to be input. The program calculates teh subtotal,
#   sales tax (assuming 7% tax), and total cost of the purchase and displays
#   those values to the user. The program allows for prices to be input as
#   integers or decimals. Prices may include a '$' and commas.

# References:
# Lysecky, et al. (2019). CSC500: principles of programming. zyBooks.
#   https://learn.zybooks.com/zybook/CSC500zyBookInteractiveText2020
#//////////////////////////////////////////////////////////////////////////////
def display_instructions(): # Provides program purpose to user
    print("You may enter the price of any number of retail items.")
    print("This program will calculate the subtotal, sales tax (assuming tax \
is 7%), and the total price of the sale.")
    return
#//////////////////////////////////////////////////////////////////////////////
# This function prompts user to input item prices and instructs user to enter
#   'f' when finished entering prices. After each user input, function checks
#   whether input is a valid price, 'f', or an invalid entry (anything else).

def get_user_input():
    list_prices = [] # Initialize empty list of user-entered prices
    user_input = ''
    while user_input != 'f':
        user_input = input("Enter item price or 'f' when finished:\n")
        # Remove dollar sign and commas if they were entered as part of the
        #   item price
        user_input = user_input.replace('$','')
        user_input = user_input.replace(',','')

        # If user entered 'f', exit loop
        if user_input == 'f':
            break

        # Else if user entered invalid input
        #   (i.e. user entered not 'f' and not a number)
        #   display error message
        elif user_input.replace('.','').isnumeric() == False:
            print("That is not a valid input. Please try again.")

        # Else (entry is valid price) convert input to float, add to list_items
        else:
            item_price = float(user_input)
            list_prices.append(item_price)

    return list_prices
#//////////////////////////////////////////////////////////////////////////////
# This function calculates the subtotal, sales tax, and total cost
def do_math(list_prices):
    subtotal = sum(list_prices)
    tax_rate = 0.07 # 7% sales tax. Adjust this value for desired tax %
    sales_tax = tax_rate * subtotal
    total = subtotal + sales_tax
    return subtotal, sales_tax, total
#//////////////////////////////////////////////////////////////////////////////
# This function displays results to the user
def display_results(subtotal, sales_tax, total):
    print("The subtotal is ${:.2f}".format(subtotal))
    print("The sales tax is ${:.2f}".format(sales_tax))
    print("Your total comes out to ${:.2f}".format(total))
#//////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    display_instructions()
    list_prices = get_user_input()
    subtotal, sales_tax, total = do_math(list_prices)
    display_results(subtotal, sales_tax, total)
