import sys


def isPrime(number):
	if number <= 3:
		return True;

	for x in range(2,number-1):
		if number%x == 0:
			return False;
	return True;


def getAPrimeFactor(number):
	x = 1
	while (x < number):
		x+=1;
		if isPrime(x):
			if number%x == 0:
				return x
	return number


if __name__ == '__main__':
	
	nCurrentValue = 600851475143 

	nLargestPrime = 0;
	while(True):
		nPrimeFactor = getAPrimeFactor(nCurrentValue);
		
		
		if(nPrimeFactor > nLargestPrime):
			nLargestPrime = nPrimeFactor
		if(nPrimeFactor == nCurrentValue):
			break;
		nCurrentValue = nCurrentValue/nPrimeFactor;
		
	print  nLargestPrime

	
