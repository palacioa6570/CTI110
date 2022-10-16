    # Displaying results differently
    # 10/12/22
    # CTI-110 P2HW1 - Travel
    # Anneliese Palacios
    #
budget = float(input('Enter your budget:\n')) #getting budget from input
destination = input('Enter your desired destination:\n') #getting destination from input
gas_price = float(input('How much money do you expect to spend on gas?\n')) #getting gas cost from input
acco = float(input('What is the approximate total cost of accomodations?\n')) #getting cost of accomodations from input
food = float(input('How much will you spend on food?\n')) #getting food cost from input
expenses = gas_price + acco + food #adding all expenses
total_cost = budget - expenses #subtracting expenses from budget
print('-------Travel Expenses-------')
print('Location:'+'{:>19}'.format(destination)) #printing location, aligning to right length 19
print(f"Set Budget:{f'${budget}':>15}") #printing budget, aligning to right length 15
print(f"\nGas:{f'${gas_price}':>21}", f"\nAccomodations:{f'${acco}':>11}", f"\nFood:{f'${food}':>20}") #printing gas, accomodations, and food with right alignments 21, 11, and 20
print('-----------------------------\nRemaining Balance:', f'${total_cost}') #printing total cost
