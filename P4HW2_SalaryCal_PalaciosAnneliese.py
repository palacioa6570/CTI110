# CTI-110
# P4HW2 - Salary Calculator
# Anneliese Palacios 
# 11/28/2022
# This program will take the employee's name, hours worked, and pay rate
# It will calculate the amount of overtime, overtime pay, and then total pay
# Program will then display data in a table, once the loop is complete it will print combined employee information
#

num_emp = 0         # variable holds total number of employees inputed into program
totalOvertimep = 0  # variable holds total overtime pay of employees inputed into program
totalRegp = 0       # variable holds total regular pay of employees inputed into program
totalGrossp = 0     # variable holds total gross pay of employees inputed into program

# this loop will continue to run until user inputs the sentinel 'None'
while True:
    # will take inputs of name, hours and pay rate
    employee_name = input('Enter employee\'s name or "None" to terminate: ')
    # if the input is 'None' it will break the loop
    if employee_name == 'None':
        break
    else:
    # else it will just add an employee to the total
        num_emp += 1
            
    employee_hours = float(input('How many hours did ' + employee_name + ' worked?: '))
    employee_payrate = float(input('What is ' + employee_name + '\'s pay rate?: '))
    # variables to calculate values inputed
    overtime = 0
    overtimepay = 0
    overtimerate = 0
    did_overtime = False
    regpay = 0
    grosspay = 0

    # checks to see if employee's work hours is less than 40
    # if so, it will just calculate regular pay and gross pay
    if employee_hours <=40:
      did_overtime = False
      regpay = employee_hours * employee_payrate
      overtime = 0
      overtimepay = 0
      overtimerate = 0
      grosspay = regpay
    else:
    #else it will calculate the overtime as well as reg pay and gross pay
      did_overtime = True
      overtime = employee_hours - 40
      overtimerate = employee_payrate * 1.5
      overtimepay = overtime * overtimerate
      regpay = employee_payrate * 40
      grosspay = overtimepay + regpay

    # these lines add the inputed employee's overtime pay, regular pay, and gross pay into the variables
    # this will add onto with each employee inputed
    totalOvertimep += overtimepay
    totalRegp += regpay
    totalGrossp += grosspay

    # printing the table
    print('----------------------------------------')
    print('Employee Name:'+'{:>15}'.format(employee_name))
    print('\nHours Worked', '{:>10}'.format('Pay Rate'), '{:>10}'.format('OverTime'), '{:>14}'.format('OverTime Pay'), '{:>13}'.format('RegHour Pay'), '{:>11}'.format('Gross Pay'))
    print('--------------------------------------------------------------------------------------')
    print(employee_hours, '{:>15}'.format(f"${employee_payrate:.2f}"), '{:>8}'.format(overtime), '{:>14}'.format(f"${overtimepay:.2f}"), '{:>14}'.format(f"${regpay:.2f}"), '{:>13}'.format(f"${grosspay:.2f}"))
    print()
# when the loop is terminated the program will print the number of employees, total overtime pay, total regular pay, and total gross pay
print()
print('Total number of employees entered:', num_emp)
print(f'Total amount payed for overtime: ${totalOvertimep:.2f}')
print(f'Total amount payed for regular hours: ${totalRegp:.2f}')
print(f'Total amount payed in gross: ${totalGrossp:.2f}')
