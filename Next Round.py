list_Input=list(map(int,input().split()))
x= list_Input[0]
y=list_Input[1]
score_Value = list(map(int,input().split()))

value= score_Value[y-1]
i=0
count=0
while i<x:
    if value==0 :
        if value< score_Value[i]:
            count += 1
    else:
        if value <= score_Value[i]:
            count += 1

    i+=1
print(count)