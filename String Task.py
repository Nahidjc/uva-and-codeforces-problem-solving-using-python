vowel =['a','A','E','e','I','i','O','o','U','u','Y','y']
value=input()
L = list(value)
finaloutput=''
i=0
while i<len(value):
    if value[i] in vowel:
        pass
    else:
        finaloutput=finaloutput+'.'+(value[i].lower())

    i+=1
print(finaloutput)

