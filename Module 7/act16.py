b = 5000
total_amount = 0
for i in range(12):
	p = (b*2)/100
	total_amount = total_amount + p
	ub = b - p
	print(b,round(p),ub)
	b = ub + (ub*1.5)/100
print(total_amount, b)