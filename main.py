n = int(input())
adict = {}
for i in range(n):
	data = input()
	k, v = data.split()
	v = int(v)
	if k not in adict:
		adict[k] = [v]
	else:
		adict[k].append(v)
print(adict)