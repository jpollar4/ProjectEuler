import csv;
import jeffutils;


dictNameValues = {"A":1, "B":2,"C":3, "D":4,"E":5, "F":6,"G":7, "H":8,"I":9, "J":10,"K":11, "L":12,"M":13, "N":14,"O":15, "P":16,"Q":17, "R":18,"S":19, "T":20,"U":21, "V":22,"W":23, "X":24,"Y":25, "Z":26};

def getNameValue(strName):
	nResult = 0;
	for i in strName:
		nResult +=int(dictNameValues[i]);

	return nResult





listNames = []

f = open('ProjectEuler22_names.txt')
reader = csv.reader(f)
for row in reader:
	for i in row:
		listNames.append(i)

sortedList = jeffutils.mergeSort(listNames);

f.close()

nAnswer = 0

for i in sortedList:
	nPlace = sortedList.index(i) + 1;
	nValue = getNameValue(i);
	nNameValue = nValue*nPlace;
	nAnswer += nNameValue;

print nAnswer



