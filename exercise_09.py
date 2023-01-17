##https://www.w3schools.com/python/ref_string_join.asp
## tried append from java, found this on w3schools, works by seperating the with the first part between second.
## can use to make sentance

words = list()
for x in range(5):
    words.append(input('Please enter a word: '))
sentance= ' '.join(words)
print('Words: ', words)
print('One String: ', sentance)