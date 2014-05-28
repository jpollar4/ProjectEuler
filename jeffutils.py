import sys
#returns true or false
def isPrime(number):
	if number <= 3:
		return True;
	
	if number%2 == 0:
		return False;

	#not divisible by a known prime	
	for x in range(3, int(number**0.5)+1, 2):
		if number%x == 0:
			return False;
	return True;
