    #Program calculates an employee's salary including overtime (if there is any)
    #10/23/22
    #CTI-110 P3HW2 - Salary Calculator
    #Anneliese Palacios

employee_name = input('Enter employee\'s name: ')
employee_hours = float(input('Enter number of hours worked: '))
employee_payrate = float(input('Enter employee\'s pay rate: '))
overtime = 0
overtimepay = 0
overtimerate = 0
did_overtime = False
regpay = 0
grosspay = 0

if employee_hours <=40:
  did_overtime = False
  regpay = employee_hours * employee_payrate
  overtime = "N/A"
  overtimepay = "N/A"
  overtimerate = "N/A"
  grosspay = pay
else:
  did_overtime = True
  overtime = employee_hours - 40
  overtimerate = employee_payrate * 1.5
  overtimepay = overtime * overtimerate
  regpay = employee_payrate * 40
  grosspay = overtimepay + regpay

print('----------------------------------------')
print('Employee Name:'+'{:>15}'.format(employee_name))
print('\nHours Worked', '{:>10}'.format('Pay Rate'), '{:>10}'.format('OverTime'), '{:>14}'.format('OverTime Pay'), '{:>13}'.format('RegHour Pay'), '{:>11}'.format('Gross Pay'))
print('--------------------------------------------------------------------------------------')
print(employee_hours, '{:>15}'.format(f"${employee_payrate:.2f}"), '{:>8}'.format(overtime), '{:>14}'.format(f"${overtimepay:.2f}"), '{:>14}'.format(f"${regpay:.2f}"), '{:>13}'.format(f"${grosspay:.2f}"))
