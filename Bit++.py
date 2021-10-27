n = int(input())
count=0
i=0
while i<n:
    bitland=input()
    if bitland== 'X++' or bitland == '++X':
        count +=1
    elif bitland== 'X--' or bitland == '--X':
        count-=1
    i+=1

print(count)