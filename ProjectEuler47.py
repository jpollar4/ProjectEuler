import jeffutils;


def hasDistinctFactors(number,nFactors):
	factors = jeffutils.getPrimeFactors(number);
	uniqueFactors = [];
	for i in factors:
		if i not in uniqueFactors:
			uniqueFactors.append(i);
	if(uniqueFactors.__len__() == nFactors):
		return True;
	return False;




if __name__ == '__main__':


	nCurNumber = 134000;
	while(True):
		print nCurNumber
		if(hasDistinctFactors(nCurNumber,4)):
			print "~~1~~~~~~~~~~~~"
			nCurNumber+=1;
			if(hasDistinctFactors(nCurNumber,4)):
				print "~~2~~~~~~~~~~~~"
				nCurNumber+=1;
				if(hasDistinctFactors(nCurNumber,4)):
					print "~~3~~~~~~~~~~~~"
					nCurNumber+=1;
					if(hasDistinctFactors(nCurNumber,4)):
						print "~~~~~~~~~~~~~~~~~"
						print nCurNumber-3
						break;
		else:
			nCurNumber+=1;




