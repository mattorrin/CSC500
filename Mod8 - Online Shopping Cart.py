## CSC500-1
## Program: Online Shopping Cart
## Author: Matt Orrin
## Description:
##        This program uses classes ItemToPurchase and ShoppingCart to emulate an online
##        shopping cart. Each item inputted has price, quantity, and description. User can
##        add, remove, modify, and view items in the cart.  


#Attributes of each item created, with initializers
class ItemToPurchase:
    def __init__(self, item_name='none',
                 item_price = 0.0,
                 item_quantity = 0,
                 item_desc='none'):
        
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_desc = item_desc

    #Determines the cost for the quantity of each item
    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}')

    def print_item_desc(self):
        print(f'{self.item_name}: {self.item_desc}')

#ShoppingCart maintains a list of items that can be manipulated
class ShoppingCart:
    def __init__(self, customer_name= 'none', current_date= 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    #Adds new items to cart
    def add_item(self, new_item):
        print(f'\nAdding {new_item.item_name} to cart')
        self.cart_items.append(new_item)

    #As long as items exist, item will be removed from cart
    def remove_item(self, item_eject):
        for item in self.cart_items:                                
            if item.item_name.lower() == item_eject.lower():
                print(f'\nRemoving {item.item_name} from cart')
                self.cart_items.remove(item)
                return
        print('\nThat item isn\'t in the cart!\n')
        
    #If item in cart, user prompted with item attributes to modify.
    #Any, or all, attributes can be modified
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
        #print('\Number of Items: {}'.format(total_items))
        return total_items

    #Totals cost of items multiplied by their quantities
    def get_cost_of_cart(self):             
        total_items = 0
        for item in self.cart_items:                
                total_items += item.item_price * item.item_quantity
        return total_items

    #Displays number of items in cart and gets each items cost and quantity
    def print_total(self):                  
        print(f'\n{self.customer_name}\'s Shopping Cart - {self.current_date}')
        total_items = self.get_num_items_in_cart()
        print('Number of Items: {}'.format(total_items))
        for item in self.cart_items:
            item.print_item_cost()

    #Displays descriptions of items in cart
    def print_descriptions(self):
        print(f'\n{self.customer_name}\'s Shopping Cart:  {self.current_date}')
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        for item in self.cart_items:
           item.print_item_desc()

#Displays menu and controls cart operations, until user 'q'uits out of cart.        
def print_menu(shopping_cart):
    menu_choices = {'a': "Add item to cart",
                        'r': "Remove item from cart",
                        'c': "Change item info (price, quantity, description)",
                        'i': "Output items\' descriptions",
                        'o': "Output shopping cart",
                        'q': "Quit"}

    user_input = ''

    #Loop iterates, displaying menu, until 'q' is entered
    while user_input.lower() != 'q':    
        print('\n--MENU--')
        for option, desc in menu_choices.items():
            print(option, ' - ', desc)

        user_input = input('Choose an option: ')

        #Determines if entry is valid, loop continues to iterate if not
        if user_input.lower() not in menu_choices:
            print("\nInvalid selection!  Make valid selection")

        elif user_input.lower() == 'q':
            print(f"\nThanks for Shopping with us, {customer_name}!")

        #Gets item attributes to ItemToPurchase and then added to cart
        elif user_input.lower() == 'a':
            name = input("\nEnter the item name: ").strip()
            price = float(input('Enter the item price: '))
            quantity = int(input('Enter the quantity: '))
            desc = input("Enter the description of the item: ")
            new_item = ItemToPurchase(name, price, quantity, desc)
            shopping_cart.add_item(new_item)

        #Checks if cart has items, lists items then lets user remove an item
        elif user_input.lower() == 'r':
            if shopping_cart.get_num_items_in_cart() == 0:
                print('\nSHOPPING CART IS EMPTY')

            else:
                shopping_cart.print_total()
                item_eject = input('\nItem to remove from cart: ')
                shopping_cart.remove_item(item_eject)

        #Checks if cart has items, lists them then lets user modify item and its attributes
        elif user_input.lower() == 'c':
            if shopping_cart.get_num_items_in_cart() == 0:
                print('\nSHOPPING CART IS EMPTY')

            else:
                shopping_cart.print_total()
                mod_item = input('\nItem that needs to be modified: ').strip()
                price_change = (input('Enter new price - Enter for no change: '))
                quantity_amt = (input('Enter new quantity - Enter for no change: '))  
                new_desc = input('Enter new description - Enter for no change: ')

                #Determines if user hits enter to not change attributes and maintain item
                #initializations. Otherwise, new attributes get passed to ItemToPurchase
                new_quantity = int(quantity_amt) if quantity_amt.strip() != '' else '0'
                new_price = float(price_change) if price_change.strip() != '' else 0.0
                new_desc = new_desc if new_desc.strip() != '' else 'none'

                temp_mod = ItemToPurchase(item_name = mod_item,
                                          item_price = new_price,
                                          item_quantity = new_quantity,
                                          item_desc = new_desc)
                shopping_cart.modify_item(temp_mod)

        #Checks if cart has items, lists descriptions  if cart not empty
        elif user_input.lower() == 'i':
            if shopping_cart.get_num_items_in_cart() == 0:
                print('\nSHOPPING CART IS EMPTY')
            else:
                shopping_cart.print_descriptions()

        #Checks if cart has items, outputs cart total
        elif user_input.lower() == 'o':
            if shopping_cart.get_num_items_in_cart() == 0:
                print('\nSHOPPING CART IS EMPTY')
            else:
                shopping_cart.print_total() 
                cost_total = shopping_cart.get_cost_of_cart()
                print('Total: ${:.2f}'.format(cost_total))

        

if __name__ == "__main__":
    customer_name = input("\nEnter your name: ")
    current_date = input("Enter today\'s date: ")
    print('\nWelcome, {}. \nToday\'s date: {}'.format(customer_name, current_date))

    #Creates a shopping cart for new user
    shopping_cart = ShoppingCart(customer_name, current_date)

    #Calls for menu system to operate the cart
    print_menu(shopping_cart)         

    


