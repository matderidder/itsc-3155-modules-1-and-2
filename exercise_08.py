##https://www.w3schools.com/python/ref_list_count.asp
## the count function on w3schools counts the number of times an element is in the list, used to find if an element is repeated
orignial = list()
unique = list()
for i in range(0,10):
    print(i+1,'.')
    orignial.insert(i,float(input("Enter a number for the list: ")))
print('Orignial List: ', orignial)
for nums in orignial:
    x = orignial.count(nums)
    if(x < 2):
        unique.append(nums)
print('Nums that apear once: ', unique)
