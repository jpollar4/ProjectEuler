import math
import jeffutils
if __name__ == '__main__':

	
	nSum = 2;
	nCurrentNumber = 3;
	while(nCurrentNumber < 2000000):		
		if jeffutils.isPrime(nCurrentNumber):
			
			nSum +=	nCurrentNumber;
			print nCurrentNumber
		nCurrentNumber+=2;


	print "~~~~~~" + str(nSum);
	
	
		