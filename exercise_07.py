numbers = list()
evens = list()
i = 0
info = ''
while(info != 'QUIT'):
    info = input('Please enter a number or QUIt to quit: ')
    if(info  != 'QUIT'):
        numbers.insert(i, info)
        i = i+1
print(numbers)
j = 0
for i in numbers:
    if (int(i) % 2) == 0:
        evens.insert(j,i)
        j = j+1
print(evens)