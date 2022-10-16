    #Program takes inputs and prints a receipt with 15% tip
    #10/16/22
    #CTI-110 P2HW2 - Receipt Calculator, part 2
    #Anneliese Palacios
food_item = input('Enter name of food item:\n')
food_price = float(input('Enter price of food item:\n'))
item_quantity = int(input('Enter quantity of item:\n'))
price = food_price * item_quantity

food_item2 = input('Enter name of second food item:\n')
food_price2 = float(input('Enter price of second food item:\n'))
item_quantity2 = int(input('Enter quantity of second food item:\n'))
price2 = food_price2 * item_quantity2

total = price + price2
print('----Receipt----\n', item_quantity, food_item, f'@ ${food_price:.2f}',f'= ${price:.2f}\n', item_quantity2, food_item2, f'@ ${food_price2:.2f}', f'= ${price2:.2f}')
print('\nTotal cost:', f'${total:.2f}')

gratuity = total * .15
print('\n15% gratuity:', f'${gratuity:.2f}')
print('Total with tip:', f'${total + gratuity:.2f}')
