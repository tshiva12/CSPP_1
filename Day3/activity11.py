varA=int(input("enter a value"))
varB=(input("enter a value"))
if(type(varA)==str or type(varB)==str):
	print("strings involved")
elif(varA>varB):
	print("varA is larger than varB")
elif(varA==varB):
	print("varA is equal to varB")
else:
	print("varA is smaller than varB")