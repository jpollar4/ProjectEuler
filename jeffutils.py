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


def getPrimeFactors(number):

	factors = [];

	while (number%2 == 0):
		number = number/2;
		factors.append(2);
    
	for i in range(3,number, 2):
		while(number%i==0):
			factors.append(i);
			number = number/i;

	if(number>2):
		factors.append(number);
	
	return factors
