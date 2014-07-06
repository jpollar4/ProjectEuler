def sumOfDivisors(number):
	divisors = [1];
	for i in range(2,number):
		if(number%i==0):
			divisors.append(i);

	nResult = 0;
	for i in divisors:
		nResult +=i;

	return nResult

def getAmicable(number):
	nFirst = sumOfDivisors(number);

	if(sumOfDivisors(nFirst) == number and nFirst !=number):
		return nFirst;

	return -1;


amicableNumbers = [220,284]

for i in range(1,10001):
	print i
	if i not in amicableNumbers:
		nPossibleAmicable = getAmicable(i);
		if nPossibleAmicable != -1:
			amicableNumbers.append(i);
			if nPossibleAmicable not in amicableNumbers:
				amicableNumbers.append(nPossibleAmicable);

print amicableNumbers

nAnswer = 0;
for i in amicableNumbers:
	nAnswer+=i;

print nAnswer;

