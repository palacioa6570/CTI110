    #Program takes inputs and prints a receipt
    #10/8/22
    #CTI-110 P2LAB2 - Receipt Calculator
    #Anneliese Palacios
food_item = input('Enter name of food item:\n')
food_price = float(input('Enter price of food item:\n'))
item_quantity = int(input('Enter quantity of item:\n'))
price = food_price * item_quantity
print('----Receipt----\n', item_quantity, food_item, f'@ ${food_price:.2f}',f'= ${price:.2f}')
print('\nTotal cost:', f'${price:.2f}')
