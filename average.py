a = int(input("Enter marks of eng:"))
b = int(input("Enter marks of hindi:"))
c = int(input("Enter marks of marathi:"))
d = int(input("Enter marks of hist:"))
e = int(input("Enter marks of sci:"))

total = a+b+c+d+e/5
print("Total marks=",total)



if(total >= 400):
	print("A Grade")
elif(total >= 300 and total < 400):
	print("B Grade")
elif(total >= 250 and total < 300):
	print("C Grade")
elif(total >= 200 and total < 250):
	print("D Grade")
else:
	print("E Grade")
