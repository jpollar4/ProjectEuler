

if __name__ == '__main__':

	nLongestChain = 0;
	nBestNumber = 0;

	for i in range(1,1000001, 2):
		print i;
		nCurValue = i
		nCurChainLength = 0;
		while(True):
			
			if(nCurValue%2==0):
				nCurValue = nCurValue/2;
				nCurChainLength+=1;
			else:
				nCurValue = (3*nCurValue)+1;
				nCurChainLength+=1;
			if(nCurValue == 1):
				break;

		if(nCurChainLength > nLongestChain):
			nLongestChain = nCurChainLength;
			nBestNumber = i

	print "~~~"
	print nLongestChain;
	print nBestNumber;
