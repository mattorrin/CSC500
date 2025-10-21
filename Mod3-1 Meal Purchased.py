import math

#This function displays the menu for each category
def menu_display(course):
    for item, price in course.items():
            print(f"{item}: ${price:.2f}")
    return course        

#Establish a dictionary of menu categories
sides_menu = {"1 - Fries": 3.50, "2 - Tots": 3.50, "3 - Beans": 4.00, "4 - No side ": 0.00}
entree_menu = {"1 - Beyond Dog": 5.00, "2 - Beyond Burger": 6.50, "3 - Beyond Chix Sandwich": 7.00, "4 - No entree": 0.00} 
drink_menu = {"1 - Soda": 2.00, "2 - Fresh Lemonade": 3.50, "3 - Coffee": 2.00, "4 - No drink/Water": 0.00}

print("Thanks for dining at \'A Bev & Beyond Meat\' \nMake sure to pick a side, entree & drink:\n")

#Ensure that inputs are correct values
while True:
    try:
        print("\n---SIDES--- \n")
        menu_display(sides_menu)
        side_order = int(input("\nPick which side you would like: \n"))
        if 0 < side_order <= len(sides_menu):           
            print('\n---> You ordered', list(sides_menu.keys())[side_order-1],' <---')
            break
        else:
            print('Not a valid entry, please try again!\n') 
    except ValueError:
        print('Not a valid entry, please try again!\n')
        
while True:
    try:
        print("\n---ENTREES--- \n")
        menu_display(entree_menu)
        entree_order = int(input("\nPick which entree you would like: \n"))
        if 0 < entree_order <= len(entree_menu):
            print('\n---> You ordered', list(entree_menu.keys())[entree_order-1],' <---')
            break
        else:
            print('Not a valid entry, please try again!\n') 
    except ValueError:
        print('Not a valid entry, please try again!\n')
        
while True:
    try:
        print("\n---Drinks--- \n")
        menu_display(drink_menu)
        drink_order = int(input("\nPick which drink you would like: \n"))
        if 0 < drink_order <= len(drink_menu):
            print('\n ---> You ordered', list(drink_menu.keys())[drink_order-1],' <---')
            break
        else:
            print('Not a valid entry, please try again!\n') 
    except ValueError:
        print('Not a valid entry, please try again!\n')

#These will pull the value for each category based on user inputted numbers
side_item = list(sides_menu.keys())[side_order-1]
side_cost = float(list(sides_menu.values())[side_order-1])
                  
entree_item = list(entree_menu.keys())[entree_order-1]
entree_cost = float(list(entree_menu.values())[entree_order-1])

drink_item = list(drink_menu.keys())[drink_order-1]
drink_cost = float(list(drink_menu.values())[drink_order-1])

subtotal = float(side_cost + entree_cost + drink_cost)
tip_amount = subtotal * 0.18
tax_amount = subtotal * 0.07
bill_total = subtotal + tax_amount + tip_amount 

print(f"\nYou ordered\n #", side_item, "\n #", entree_item, "\n #", drink_item, "\n")
print(f"Your cost, before tax (7%) & tip (18%) is : ${subtotal:.2f}")      
print('Tax (7%) = ${:.2f}, and Tip (18%) = ${:.2f}'.format(tax_amount, tip_amount))
print('Your bill total is ${:.2f}'.format(bill_total))

