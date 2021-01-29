# CSC 500, Module 3: Portfolio Project Milestone 1 - Option #1
# Created by Matt Reilly. 15 Jan 2021

# References:
# Lysecky, et al. (2019). CSC500: principles of programming. zyBooks.
#   https://learn.zybooks.com/zybook/CSC500zyBookInteractiveText2020
#//////////////////////////////////////////////////////////////////////////////
def display_instructions():
    print('This program allows you to enter the name, price, and quantity of \
two items. ')
    print('This program will display the total for each item and for both \
items combined.\n')
    return
#//////////////////////////////////////////////////////////////////////////////
# Create object class for items to be purchased
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, \
self.item_price, self.item_price * self.item_quantity))
        return
#//////////////////////////////////////////////////////////////////////////////
# Calculate cost of each item, then calculate total cost of both items
def compute_cost(item1, item2):
    item1_cost = item1.item_price * item1.item_quantity
    item2_cost = item2.item_price * item2.item_quantity
    total_cost = item1_cost + item2_cost
    return total_cost
#//////////////////////////////////////////////////////////////////////////////
# Display item names, prices, quantities and totatl cost to user
def display_results(item1, item2, total_cost):
    print('\nTOTAL COST')
    print('{}: {} @ ${:.2f} = ${:.2f}'.format(item1.item_name, \
    item1.item_quantity, item1.item_price, item1.item_price * item1.item_quantity))
    print('{}: {} @ ${:.2f} = ${:.2f}'.format(item2.item_name, \
    item2.item_quantity, item2.item_price, item2.item_price * item2.item_quantity))
    print('Total: ${:.2f}'.format(total_cost))
    return
#//////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    display_instructions()
    item1 = ItemToPurchase()
    print('Item 1')

    # Get item 1 information from user
    item1.item_name = input('Enter the item name:\n')

    # Ensure price and quantity entries are valid (both must be numbers,
    #   quantity must be an integer). This loop prompts for price input until
    #   user input is valid. Dollar signs are acceptable in the price input

    while True:
        # Remove dollar sign in case user entered one
        item_price = input('Enter the item\'s price:\n').replace('$','')
        try:
            item1.item_price = float(item_price)
        except ValueError:
            print('Invalid price entry. Please try again.\n')
            continue
        break

    # Prompts user for quantity until user provides a valid quantity
    while True:
        try:
            item1.item_quantity = int(input('Enter the item quantity:\n'))
        except ValueError:
            print('Invalid quantity. Please try again.\n')
            continue
        break

    # Create item 2 and get user-entered info
    item2 = ItemToPurchase()
    print('\nItem 2')
    item2.item_name = input('Enter the item name:\n')

    while True:
        # Remove dollar sign in case user entered one
        item_price = input('Enter the item\'s price:\n').replace('$','')
        try:
            item2.item_price = float(item_price)
        except ValueError:
            print('Invalid price entry. Please try again.\n')
            continue
        break

    # Prompts for quantity until user enters a valid quantity
    while True:
        try:
            item2.item_quantity = int(input('Enter the item quantity:\n'))
        except:
            print('Invalid quantity. Please try again.\n')
            continue
        break

    total_cost = compute_cost(item1, item2)
    display_results(item1, item2, total_cost)
