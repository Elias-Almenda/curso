import decimal

num1 = decimal.Decimal('0.1')
num2 = decimal.Decimal('0.7')

num3 = num1 + num2
print(num3)
print(f'{num3:.2f}')

# round
print(round(num3, 2))

# decimal so em casos ultra especificos em que precisa ate a ultima casa