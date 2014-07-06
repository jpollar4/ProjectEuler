def factorial(number):
	nCurrentInt = number;
	nResult = number;

	while(nCurrentInt > 1):
		nCurrentInt-=1;
		nResult*=nCurrentInt;

	return nResult


def sumDigits(number):
	strNumber = str(number);
	nResult = 0;
	for i in strNumber:
		nResult += int(i);
	return nResult;



nFactorial = factorial(100);
nAnswer = sumDigits(nFactorial);

print nAnswer
