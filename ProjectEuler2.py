import sys




if __name__ == '__main__':
	total = 0;
	
	previousTerm=0;
	currentTerm=1;
	while currentTerm < 4000000:
		temp = currentTerm
		currentTerm += previousTerm;
		if currentTerm%2==0:
			total+=currentTerm;
		previousTerm = temp;
	print total
