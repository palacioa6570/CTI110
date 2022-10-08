''' Type your code here. '''
gas_mileage = float(input())
gas_costpg = float(input())
cost_pm = gas_costpg * (1/gas_mileage)

miles_tw = 20 * cost_pm
miles_se = 75 * cost_pm
miles_fi= 500 * cost_pm
print(f'{miles_tw:.2f} {miles_se:.2f} {miles_fi:.2f}')
