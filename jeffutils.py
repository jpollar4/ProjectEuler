import sys
#returns true or false
def isPrime(number):
	if number <= 3:
		return True;
	
	if number%2 == 0:
		return False;

	#not divisible by a known prime	
	for x in range(3, int(number**0.5)+1, 2):
		if number%x == 0:
			return False;
	return True;


def getPrimeFactors(number):

	factors = [];

	while (number%2 == 0):
		number = number/2;
		factors.append(2);
    
	for i in range(3,number, 2):
		while(number%i==0):
			factors.append(i);
			number = number/i;

	if(number>2):
		factors.append(number);
	
	return factors



def mergeSort(unsortedList):
	if unsortedList.__len__() == 1:
		return unsortedList;


	listLeft = [];
	listRight = [];
	nMiddle = unsortedList.__len__() / 2;

	for i in range(0,nMiddle):
		listLeft.append(unsortedList[i])
	for i in range(nMiddle, unsortedList.__len__()):
		listRight.append(unsortedList[i]);

	left = mergeSort(listLeft);
	right = mergeSort(listRight);


	sortedList = mergeSort_merge(left,right);

	return sortedList;

def mergeSort_merge(left, right):
	mergedList = [];
	while left.__len__() > 0 or right.__len__() > 0:
		if left.__len__() > 0 and right.__len__() > 0:          
			if left[0] <= right[0]:
				mergedList.append(left[0]);
				left.pop(0)
			else:
				mergedList.append(right[0]);
				right.pop(0);
		elif left.__len__() > 0:
			mergedList.append(left[0]);
			left.pop(0)
		elif right.__len__() > 0:
			mergedList.append(right[0]);
			right.pop(0);

	
	return mergedList;

