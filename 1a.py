dele=[]
string= input("Enter any string: ")
ele =('a','e','i','o','u')
for x in string.lower():
    if x in ele:
        dele.append(x)
        newstr = string.replace(x," ")
print(f'New string is: {newstr} from {string}')
print(f'Deleted are: {dele}')