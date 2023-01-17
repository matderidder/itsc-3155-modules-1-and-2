st = input('Please enter a word: ')
split = list(st)
allList = list()
for i in range(0,len(split),3):
    minlist = list()
    for j in range(3):
        if((i+j) < len(split)):
            minlist.append(split[i+j])
    allList.append(minlist)
print(allList)