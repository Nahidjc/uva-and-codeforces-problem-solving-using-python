color=['R','G','B']
n=int(input())
value=input()
i=1
totalCount=[]
count=0
if n==1:
    print(0)
else:
    while i < n:
        if value[i - 1] == value[i]:
            count += 1
            # if i == n - 1:
            #     totalCount.append(count)
        # elif value[i - 1] != value[i]:
        #     totalCount.append(count)
        #     count = 0
        i += 1
    print(count)