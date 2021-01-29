#

class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, \
self.item_price, self.item_price * self.item_quantity))
        return



if __name__ == '__main__':
    water = ItemToPurchase()
