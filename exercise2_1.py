##https://www.w3schools.com/python/ref_list_reverse.asp
## found this to use as a reverse on a list changed string then revert it to a string
st = input('Please enter a string: ')
re = list(st)
re.reverse()
ts = ''.join(re)
print(ts)