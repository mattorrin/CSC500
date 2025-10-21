#Online shopping cart allows a user to maintain a cart of items, prices, quantities and descriptions

#Attributes of each item, with initializers
class ItemToPurchase:
    def __init__(self, item_name='none',
                 item_price = 0.0,
                 item_quantity = 0,
                 item_desc='none'):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_desc = item_desc

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}')

    def print_item_desc(self):
        print(f'{self.item_name}: {self.item_desc}')

#ShoppingCart maintains a list of items
class ShoppingCart:
    def __init__(self, customer_name= 'none', current_date= 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, new_item):
        print(f'\nAdding {new_item.item_name} to cart')
        self.cart_items.append(new_item)

#Goes through all items in cart, if an item in cart matches input then it gets removed
    def remove_item(self, item_eject):
        for item in self.cart_items:                                
            if item.item_name.lower() == item_eject.lower():
                print(f'\nRemoving {item.item_name} from cart')
                self.cart_items.remove(item)
                return
        print('\nThat item isn\'t in the cart!\n')
        
#Goes through all items in cart, checks for item in cart. If item in cart, it compares each attribute
#to its initializers.  If they are different, then the new value gets passed to ItemToPurchase.
#Otherwise, item is not in cart.
    def modify_item(self, mod_item):
        in_cart = False
        for item in self.cart_items:
            if item.item_name.lower() == mod_item.item_name.lower():
                in_cart = True
                print(f'\nModifying {item.item_name} in cart\n')
                if mod_item.item_price != 0.0:
                    item.item_price = mod_item.item_price
                if mod_item.item_quantity != 0:
                    item.item_quantity = mod_item.item_quantity
                if mod_item.item_desc != 'none':
                    item.item_desc = mod_item.item_desc
                break
        if not in_cart:
                print('\nItem not found in cart. Nothing modified.')

#Totals all item quantities
    def get_num_items_in_cart(self):
        total_items = 0
        for items in self.cart_items:
            total_items += items.item_quantity
        print('Number of Items: {}'.format(total_items))
        return total_items

#Totals cost of items multiplied by their costs
    def get_cost_of_cart(self):             
        total_items = 0
        for item in self.cart_items:                
                total_items += item.item_price * item.item_quantity
        return total_items

#Displays number of items in cart and gets each items cost and quantity
    def print_total(self):                  
        print(f'\n{self.customer_name}\'s Shopping Cart - {self.current_date}')
        self.get_num_items_in_cart()
        for item in self.cart_items:
            item.print_item_cost()

#Displays descriptions items in cart
    def print_descriptions(self):
        print(f'\n{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart_items:
           item.print_item_desc()

#Displays menu       
def print_menu(choice):
    print('\n--MENU--')
    for option, desc in choice.items():
        print(option, ' - ', desc)

menu_choices = {'a': "Add item to cart",
                        'r': "Remove item from cart",
                        'c': "Change item quantity",
                        'i': "Output items\' descriptions",
                        'o': "Output shopping cart",
                        'q': "Quit"}

customer_name = input("\nEnter your name: ")
shopping_cart = ShoppingCart(customer_name)

#initializes menu choice
user_input = ''         

#Loop iterates until 'q' is entered
while user_input.lower() != 'q':    
    print_menu(menu_choices)
    user_input = input('Choose an option: ')
    
    if user_input.lower() not in menu_choices:
        print("\nInvalid selection!  Make valid selection")

    elif user_input.lower() == 'q':
        print(f"\nThanks for Shopping with us, {customer_name}!")

#Gets item attributes to ItemToPurchase and then added to cart
    elif user_input.lower() == 'a':
        name = input("\nEnter the item name: ")
        price = float(input('Enter the item price: '))
        quantity = int(input('Enter the quantity: '))
        desc = input("Enter the description of the item: ")
        new_item = ItemToPurchase(name, price, quantity, desc)
        shopping_cart.add_item(new_item)

    elif user_input.lower() == 'r':
        item_eject = input('\nItem to remove from cart: ')
        shopping_cart.remove_item(item_eject)

#Gets changed item attributes to ItemToPurchase and then added to cart
    elif user_input.lower() == 'c':
        mod_item = input('\nItem that needs to be modified: ')
        price_change = (input('Enter new price - Enter for no change: '))
        quantity_amt = (input('Enter new quantity - Enter for no change: '))  
        new_desc = input('Enter new description - Enter for no change: ')

#Determines if user hits enter to not change attributes and maintain item initializations
#Otherwise, new attributes get passed to ItemToPurchase
        new_quantity = int(quantity_amt) if quantity_amt.strip() != '' else '0'
        new_price = float(price_change) if price_change.strip() != '' else 0.0
        new_desc = new_desc if new_desc.strip() != '' else 'none'

        temp_mod = ItemToPurchase(item_name = mod_item,
                                  item_price = new_price,
                                  item_quantity = new_quantity,
                                  item_desc = new_desc)
        shopping_cart.modify_item(temp_mod)

    elif user_input.lower() == 'i':
        shopping_cart.print_descriptions()

    elif user_input.lower() == 'o':
        
        shopping_cart.print_total()
        cost_total = shopping_cart.get_cost_of_cart()
        print('Total: ${:.2f}'.format(cost_total))


