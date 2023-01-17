##https://www.w3schools.com/python/python_lists_add.asp 
## did not know how to add to list, looked up syntax on w3schools
## rest is checking the data
data = int(input("Enter a grade from 0 to 100: "))
if(data < 60):
    print("Your grade is F")
if(60<= data < 70):
    print("Your grade is D")
if(70<= data < 80):
    print("Your grade is C")
if(80<= data < 90):
    print("Your grade is B")
if(data > 90):
    print("Your grade is A")
