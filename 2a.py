my_list=["Habibur","Gazipur", "201-15-3242","DIU"]
chars = 0
vowels=0
for i in my_list:
    chars+=len(i)
print("Number of Characters: " ,chars, end="\n")
for i in my_list:
    for j in i:
        if j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="A" or j=="E" or j=="I" or j=="O" or j=="U":
            vowels+=1
print("Number of Vowels: ", vowels, end="\n")