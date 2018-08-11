def sumo():
	list1 = [1,2,3,[1,2,3],1,2]
	j = 0
	sumv = 0
	for i in list1:
		if type(i) == int:
			sumv = sumv + i
		else:
			k = sum(i)
			sumv = sumv + k
	print(sumv)
def main():
		sumo()
if __name__ == '__main__':
	main()
