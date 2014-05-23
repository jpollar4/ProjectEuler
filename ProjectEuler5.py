import sys
import math

if __name__ == '__main__':

	nNumberBeingTested = 380;
	bFound = False;
	while(True):
		if(bFound):
			print nNumberBeingTested;
			break;
		nNumberBeingTested+=380;
		print nNumberBeingTested;
		for x in range(1,21):
			if nNumberBeingTested%x != 0:
				break;
			if x == 20:
				bFound = True;
				break;

