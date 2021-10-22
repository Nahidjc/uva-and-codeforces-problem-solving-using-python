n = int(input())
i=0
count =0
while i<n:
    list_Input=list(map(int,input().split()))
    a=list_Input[0]
    b=list_Input[1]
    c=list_Input[2]
    if (a==1 and b==1) or  (b ==1 and c == 1) or ( a==1 and c==1):
        count+=1
    i+=1


print(count)

