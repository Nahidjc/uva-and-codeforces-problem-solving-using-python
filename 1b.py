Section_C =['Nahid','Nirob','Nahin','Tareq','Muntasir']
Section_D =['Apurbo','Izaz','Walid','Sajib','Khaled']
Section_E =['Sagor','Emon','Hasan','Ovi','Sahin']
Section_G =['Suvik','Sujon','Sakib','Siam','Sehab']

#Merge Section C and Section E and store new List
Section_C.extend(Section_E)
Section_C_and_E = Section_C

#Merge Section C and Section E
Section_D.extend(Section_G)
Section_D_and_G = Section_D

#remove last name from the list
Section_C_and_E.pop()
Section_D_and_G.pop()

#My ID is 201-15-3242 .My is last digit 2. So insert new player in index 2
Section_C_and_E.insert(2,'Tamim')
Section_D_and_G.insert(2,'Mustafizur')

print(Section_C_and_E)
print(Section_D_and_G)