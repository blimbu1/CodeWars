import sys

first_arg = sys.argv[1]

def is_prime_happy(y=first_arg):
	n = int(y)	
	if n==2 or n==1 or n==3 or n<=0 :print ("False")
	sum = 5
	for i in range(4,n):
		c = 0
		for j in range(2,i):
			if i%j==0:
				c = 1
		if c!=1:
			sum+=i
	if sum%n==0:
		print ("True")
	else:
		print("False")

if __name__ == "__main__":
	is_prime_happy()
