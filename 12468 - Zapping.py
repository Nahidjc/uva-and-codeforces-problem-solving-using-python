
while True:
    list_Input=list(map(int,input().split()))
    if list_Input[0]==-1 and list_Input[1]==-1:
        break
    else:
        x=list_Input[0]
        y=list_Input[1]
        result2=abs((x+100-y)%100)
        result3 = abs((100 - x + y) % 100)
        print(min(result2,result3))