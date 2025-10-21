item_name = input('Enter food item name:\n')

# FIXME (1): Finish reading item price and quantity, then output a receipt
item_price = float(input('Enter item price:\n'))
item_amount = int(input('Enter item quantity:\n'))
cost = float(item_price * item_amount)
print('')

print('RECEIPT')
print(f'{item_amount} {item_name} @ ${item_price:.2f} = ${cost:.2f}')
print(f'Total cost: ${cost:.2f}')
print('')
print('')

  
# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
item2_name = input('Enter second food item name:\n')
item2_price = float(input('Enter item price:\n'))
item2_amount = int(input('Enter item quantity:\n'))

cost2 = float(item2_price * item2_amount)
print('')

print('RECEIPT')
print(f'{item_amount} {item_name} @ ${item_price:.2f} = ${cost:.2f}')
print(f'{item2_amount} {item2_name} @ ${item2_price:.2f} = ${cost2:.2f}')
print(f'Total cost: ${cost + cost2:.2f}')
print('')

# FIXME (3): Add a gratuity and total with tip to the second receipt
bill_tip = (cost + cost2) * 0.15
bill_total = cost + cost2 + bill_tip
print(f'15% gratuity: ${bill_tip:.2f}')
print(f'Total with tip: ${bill_total:.2f}')
