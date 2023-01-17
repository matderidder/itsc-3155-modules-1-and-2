row = int(input('Enter a row number between 1 and 5: '))
col = int(input('Enter a col number between 1 and 5: '))
for i in range(5):
    for j in range(5):
        if (j == (col-1) and i == (row-1)):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print('\n')