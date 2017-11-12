text = "Hello World are you all."
def addAy(word):
	return(" "+word[1:]+word[0:1]+'ay' if word.isalpha() else word)
	
def piggy(text):
	y=text.split(" ")
	z=list(map(addAy,y))
	n=''.join(z)
	return(n[1:])
	

output = piggy(text)
print(output)
