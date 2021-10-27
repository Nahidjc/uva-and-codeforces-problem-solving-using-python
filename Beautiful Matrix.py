inputValue=[]
i=0
while i<5:
    inputValue.append(list(map(int,input().split())))
    i+=1

j=0
while j<5:
    k=0
    while k<5:
        if inputValue[j][k]==1:
            onePosition=abs(2-k)+abs(2-j)
        k=k+1
    j+=1
print(onePosition)