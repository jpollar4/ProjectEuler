

def getNumberString(nNumber):
	nNumber = int(nNumber)
	if(nNumber==0):
		return''
	if(nNumber==1):
		return 'one'
	if(nNumber==2):
		return 'two'
	if(nNumber==3):
		return 'three'
	if(nNumber==4):
		return 'four'
	if(nNumber==5):
		return 'five'
	if(nNumber==6):
		return 'six'
	if(nNumber==7):
		return 'seven'
	if(nNumber==8):
		return 'eight'
	if(nNumber==9):
		return 'nine'
	if(nNumber==10):
		return 'ten'
	if(nNumber==11):
		return 'eleven'
	if(nNumber==12):
		return 'twelve'
	if(nNumber==13):
		return 'thirteen'
	if(nNumber==14):
		return 'fourteen'
	if(nNumber==15):
		return 'fifteen'
	if(nNumber==16):
		return 'sixteen'
	if(nNumber==17):
		return 'seventeen'
	if(nNumber==18):
		return 'eighteen'
	if(nNumber==19):
		return 'nineteen'
		
	if(nNumber>=90):
		return 'ninety'+getNumberString(nNumber%10)
	if(nNumber>=80):
		return 'eighty'+getNumberString(nNumber%10)
	if(nNumber>=70):
		return 'seventy'+getNumberString(nNumber%10)
	
	if(nNumber>=60):
		return 'sixty'+getNumberString(nNumber%10)
	if(nNumber>=50):
		return 'fifty'+getNumberString(nNumber%10)
	if(nNumber>=40):
		return 'forty'+getNumberString(nNumber%10)
	if(nNumber>=30):
		return 'thirty'+getNumberString(nNumber%10)
	if(nNumber>=20):
		return 'twenty'+getNumberString(nNumber%10)

	
	return ''



def buildStringOfNumber(nNumber):

	stringNumber = '';
	if nNumber == 0:
		stringNumber+='zero'
	if nNumber >= 1000:
		stringNumber += 'OneThousand'
		nNumber = nNumber - 1000

	if nNumber >=100:
		stringNumber += getNumberString(str(nNumber)[0]) + 'hundred';
		nNumber= nNumber%100;
		if(nNumber != 0):
			stringNumber +='and'
	if nNumber >= 1:
		stringNumber += getNumberString(nNumber)

	

	return stringNumber


if __name__ == '__main__':

	nTargetValue = 1000
	stringNumber = '';
	for i in range(1,nTargetValue+1):
		stringNumber+= buildStringOfNumber(i);

	print stringNumber
	print stringNumber.__len__()