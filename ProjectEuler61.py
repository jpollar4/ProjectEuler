import jeffutils;

TriangleArray = [];
SquareArray = [];
PentagonalArray = [];
HexagonalArray = []; 
HeptagonalArray = [];	
OctagonalArray = [];	 
sequenceArray = [];

def isCyclic(nFirst, nSecond):
	
	return str(nFirst)[-2:] == str(nSecond)[:2];

def findCyclic(number):
	#print number

	
	for i in TriangleArray,SquareArray,PentagonalArray,HexagonalArray,HeptagonalArray,OctagonalArray:
		for n in i:
			# if n in sequenceArray:
			# 	continue;
			if isCyclic(number,n):
				return n

	return -1;




if __name__ == '__main__':

		

	nNumberTesting = 0;
	bTriangleArrayDone = False;
	bSquareArrayDone = False;
	bPentagonalArrayDone = False;
	bHexagonalArrayDone = False;
	bHeptagonalArrayDone = False;
	bOctagonalArrayDone = False;


	while(True):
		nNumberTesting+=1
		#do triangle
		if not bTriangleArrayDone:
			nTriangleValue = (nNumberTesting*(nNumberTesting+1))/2;
			if(nTriangleValue > 9999):
				bTriangleArrayDone = True;
			elif(nTriangleValue > 999):
				TriangleArray.append(nTriangleValue)
		if not bSquareArrayDone:
			nSquareValue = nNumberTesting*nNumberTesting;
			if(nSquareValue > 9999):
				bSquareArrayDone = True;
			elif(nSquareValue > 999):
				SquareArray.append(nSquareValue)
		if not bPentagonalArrayDone:
			nPentagonalValue = (nNumberTesting*(3*nNumberTesting-1))/2;
			if(nPentagonalValue > 9999):
				bPentagonalArrayDone = True;
			elif(nPentagonalValue > 999):
				PentagonalArray.append(nPentagonalValue)
		if not bHexagonalArrayDone:
			nHexagonalValue = nNumberTesting*(2*nNumberTesting-1);
			if(nHexagonalValue > 9999):
				bHexagonalArrayDone = True;
			elif(nHexagonalValue > 999):
				HexagonalArray.append(nHexagonalValue)
		if not bHeptagonalArrayDone:
			nHeptagonalValue = (nNumberTesting*(5*nNumberTesting-3))/2;
			if(nHeptagonalValue > 9999):
				bHeptagonalArrayDone = True;
			elif(nHeptagonalValue > 999):
				HeptagonalArray.append(nHeptagonalValue)
		if not bOctagonalArrayDone:
			nOctagonalValue = (nNumberTesting*(3*nNumberTesting-2));
			if(nOctagonalValue > 9999):
				bOctagonalArrayDone = True;
			elif(nOctagonalValue > 999):
				OctagonalArray.append(nOctagonalValue)

		if(bTriangleArrayDone and bSquareArrayDone and bPentagonalArrayDone and bHexagonalArrayDone and bHeptagonalArrayDone and bOctagonalArrayDone):
			break;


	
	
	for i in TriangleArray,SquareArray,PentagonalArray,HexagonalArray,HeptagonalArray,OctagonalArray:
		if sequenceArray.__len__() == 6:
			break;
		for n in i:
			if sequenceArray.__len__() == 6:
				break;
			bTriangleArrayDone=False;
			bSquareArrayDone = False;
			bPentagonalArrayDone = False;
			bHexagonalArrayDone = False;
			bHeptagonalArrayDone = False;
			bOctagonalArrayDone = False;
			del sequenceArray[:];
			nValue = n;
			sequenceArray.append(n);
			while(True):
				nCyclic = findCyclic(nValue);
				if(nCyclic == -1):
					break;
				else:
					sequenceArray.append(nCyclic);
					nValue = nCyclic
					if sequenceArray.__len__() == 6:
						if not isCyclic(sequenceArray[5],sequenceArray[0]):
							del sequenceArray[:]
						else:
							print sequenceArray
							for s in sequenceArray:							
								if not bTriangleArrayDone and s in TriangleArray:
									print str(s) + " in TriangleArray"
									bTriangleArrayDone = True;
								elif not bSquareArrayDone and s in SquareArray:
									print str(s) + " in SquareArray"
									bSquareArrayDone = True;
								elif not bPentagonalArrayDone and s in PentagonalArray:
									print str(s) + " in PentagonalArray"
									bPentagonalArrayDone = True;
								elif not bHexagonalArrayDone and s in HexagonalArray:
									print str(s) + " in HexagonalArray"
									bHexagonalArrayDone = True;
								elif not bHeptagonalArrayDone and s in HeptagonalArray:
									print str(s) + " in HeptagonalArray"				
									bHeptagonalArrayDone = True;			
								elif not bOctagonalArrayDone and s in OctagonalArray:
									print str(s) + " in OctagonalArray"
									bOctagonalArrayDone = True;
						if(bTriangleArrayDone and bSquareArrayDone and bPentagonalArrayDone and bHexagonalArrayDone and bHeptagonalArrayDone and bOctagonalArrayDone):
							break;
						else:
							del sequenceArray[:]	
							break;

	nSum = 0;
	for s in sequenceArray:
		nSum+=s					
	print sequenceArray
	print nSum
