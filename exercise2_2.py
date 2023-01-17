st = input('Please enter a string: ')
order = list()

for char in st:
    if (char.islower() ):
        order.append(char)
for char in st:
    if (char.isupper() ):
        order.append(char)
lowtoup = ''.join(order)
print(lowtoup)