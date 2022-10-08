    #Program calculates travel expenses
    #10/8/22
    #CTI-110 P1HW2 - Travel Expense
    #Anneliese Palacios
budget = float(input('Enter your budget:\n')) #getting budget from input
destination = input('Enter your desired destination:\n') #getting destination from input
gas_price = float(input('How much money do you expect to spend on gas?\n')) #getting gas cost from input
acco = float(input('What is the approximate total cost of accomodations?\n')) #getting cost of accomodations from input
food = float(input('How much will you spend on food?\n')) #getting food cost from input
expenses = gas_price + acco + food #adding all expenses
total_cost = budget - expenses #subtracting expenses from budget
print('-------Travel Expenses-------\nLocation:', destination, '\nSet Budget:', budget) #printing location and budget
print('\nGas:', gas_price,'\nAccomodations:', acco, '\nFood:', food) #printing gas, accomodations, and food
print('\nRemaining Balance:', total_cost) #printing total cost
