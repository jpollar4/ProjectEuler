
if __name__ == '__main__':

	numberArray = [];
	
	dataFile = open('ProjectEuler13_data.txt');	
	for line in dataFile:
		numberArray.append(int(line))

	nGiantSum = 0;
	for n in numberArray:
		nGiantSum +=n;

	strGiantSum = str(nGiantSum);
	strFirstTenDigits = '';

	for i in range(0,10):
		strFirstTenDigits += strGiantSum[i];	
	print strFirstTenDigits
		
		
