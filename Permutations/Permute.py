text = 'Hello'
def permutations(text):
	j = []
	j.append(text)
	b = text
	for i in range(0, len(text)):
		a = b[0]
		c = b[1:]
		for y in range(0,len(c)):
			s=c[0:y+1] + a + c[y+1:]
			if s not in j:
				j.append(s)
		b = c+a
	print(j)			

permutations(text)
