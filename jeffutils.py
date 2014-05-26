import sys
#returns true or false and an updated primeArray
def isPrime(number, primeArray):
	if number <= 3:
		return True;
	
	for i in primeArray:		
		if number%i == 0 and i!=1:
			return False;
	
	#not divisible by a known prime	
	for x in range(2,number-1):
		if number%x == 0:
			return False;
	return True;
