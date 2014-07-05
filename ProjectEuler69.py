import jeffutils;

nMax = 0;
nAnswer = 0

primeFactors = {1 : [1],2: [1,2], 3: [1,3]}



def getPrimeFactors(number):
	result = [1];

	try:
	  result = primeFactors[number]
	except KeyError:
		myFactors = jeffutils.getPrimeFactors(number);
	 	primeFactors[number] = myFactors;
	 	result = myFactors;

	return result;








def phiFunction(number):
	nPhi = 0
	theseFactors = jeffutils.getPrimeFactors(number)


	for i in range(1, number):
		myFactors = getPrimeFactors(i);
		intersection = set(theseFactors).intersection(set(myFactors));
		if intersection.__len__() == 0:
			nPhi+=1;		
			if number/nPhi < nMax:
				return 0;	
			
	return nPhi

for x in range(6,1000000, 6):
	if x%1000 == 0:
		print str(x) + "%"

	nPhi = phiFunction(x);
	if(nPhi > 0):
		nValue = x/nPhi
		if(nValue > nMax):
			nMax = nValue;
			nAnswer = x;
			print nAnswer

print nAnswer
