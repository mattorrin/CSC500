#class ItemToPurchase and initialized attributes
class ItemToPurchase:
    def __init__(self, item_name='none', item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}')

print('\nItem 1')
name1 = input("Enter the item name: ")
price1 = float(input('Enter the item price: '))
quantity1 = int(input('Enter the quantity: '))

print('\nItem 2')
name2 = input("Enter the item name: ")
price2 = input('Enter the item price: ')
quantity2 = input('Enter the quantity: ')

#Get attributes of item1 and item2
item1 = ItemToPurchase(name1, price1, quantity1)
item2 = ItemToPurchase(name2, price2, quantity2)

print('\nTOTAL COST')
item1.print_item_cost()     
item2.print_item_cost()
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

print('Total: ${:.2f}'.format(total_cost))
