def start_smoking(bars,boxes):
	total = (bars*180)+(boxes*18)
	sum1 = total
	sum2 = 0
	while (total >0):
		remain=total % 5
		total=total//5
		sum2 += remain
		sum1 += total
		print("Sum1 total is ",sum1)
		print("Remainder total is ",sum2)
	rem = 0
	while (sum2 > 0):
		sum2 = sum2 + rem
		sum1 = sum1 + sum2//5
		rem = sum2 % 5
		sum2 = sum2//5
	print ("Total smoked = ",(sum1))

start_smoking(10,2)
