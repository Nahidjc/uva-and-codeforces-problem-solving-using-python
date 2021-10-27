inputValue = input()
finalValue=''
inputSpilit= inputValue.split('+')
# intvalue = [ int(x) for x in inputSpilit ]

sortedvalue=sorted(inputSpilit)
finalValue = "+".join(sortedvalue)
print(finalValue)