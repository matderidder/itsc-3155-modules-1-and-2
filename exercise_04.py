size = int(input("Enter the size of the list: "))
numbers = list()
for i in range(0,size):
    print(i+1,'.')
    numbers.insert(i,float(input("Enter a number: ")))
print("List: ", numbers)
avg = float()
for i in range(0,len(numbers)):
    avg = avg + numbers[i]
avg = avg/len(numbers)
print("Average: ", avg )