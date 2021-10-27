updateValue=[]
i=20
while i<=60:
    if i%2==0 :
        updateValue.append(i+5)
    elif i%5==0 :
        updateValue.append(i+2)
    i+=1
print(updateValue)