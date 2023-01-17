##https://www.w3schools.com/python/ref_string_endswith.asp
## found endswith method on w3schools, using the input and an if statement to check both with or
string1 = input("Enter the first string: \n")
string2 = input("Enter the second string: ")
value1 = string1.endswith(string2)
value2 = string2.endswith(string1)
if (value1 or value2):
    print("True")
else:
    print("False")