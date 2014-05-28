#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
import jeffutils
import math

if __name__ == '__main__':
	primeArray = [2,3,5];
	nCurrentNum = 3;
	nCurrentPrime = 1;
	while(True):
		nCurrentNum+=2;
		if jeffutils.isPrime(nCurrentNum):
			nCurrentPrime = primeArray.__len__();
			primeArray.append(nCurrentNum);
			print str(nCurrentNum) + ':' + str(nCurrentPrime)
			if nCurrentPrime == 10001:
				print "~~~~~~~~"
				print nCurrentNum
				break;

		
