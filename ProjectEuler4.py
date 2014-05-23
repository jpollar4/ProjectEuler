import sys
import math

def isPalendrome(number):

	stringNumber = str(number);	
	if(stringNumber.__len__() == 1):
		return False;

	nDigitsToCheck = int(math.floor(stringNumber.__len__() / 2));
	
	for x in range(0,nDigitsToCheck):
		if stringNumber[x] != stringNumber[stringNumber.__len__() - (x+1)]:
			return False

	return True;



if __name__ == '__main__':
	nLargest = 0;
	nCurrentNumberToTest = 999;
	
	for x in reversed(range(1, nCurrentNumberToTest)):
		for i in reversed(range(1, nCurrentNumberToTest)):
			if(isPalendrome(x*i)):
				if(nLargest < (x*i)):
					nLargest = x*i;

	print nLargest
				


	
