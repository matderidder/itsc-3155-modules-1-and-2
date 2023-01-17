##https://www.w3schools.com/python/python_sets.asp
## found set command on w3schools the common list being two sets with and will get the matching elements
list1 = list()
list2 = list()
print('list1')
for i in range(0,5):
    print(i+1,'.')
    list1.insert(i,float(input("Enter a number for first list: ")))
print('\nlist2')
for i in range(0,5):
    print(i+1,'.')
    list2.insert(i,float(input("Enter a number for second list: ")))
print("List1: ", list1)
print("List2: ", list2)
commonlist = set(list1) & set(list2)
print("Common list: ", commonlist)