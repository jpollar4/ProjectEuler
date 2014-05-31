

def daysInMonth(nMonth, nYear):

	if(nMonth == 1 or nMonth == 3 or nMonth == 5 or nMonth == 7 or nMonth == 8 or nMonth == 10 or nMonth == 12):
		return 31;

	if (nMonth == 4 or nMonth == 6 or nMonth == 9 or nMonth == 11):
		return 30;

	#Febuary
	if(nYear%4!=0):
		return 28;

	if(nYear%100==0):
		if(nYear%400==0):
			return 29
		else:
			return 28

	return 29

def getMonthString(nMonth):

	if(nMonth == 1):
		return 'Jan'
	if(nMonth == 2):
		return 'Feb'
	if(nMonth == 3):
		return 'Mar'
	if(nMonth == 4):
		return 'Apr'
	if(nMonth == 5):
		return 'May'
	if(nMonth == 6):
		return 'Jun'
	if(nMonth == 7):
		return 'Jul'
	if(nMonth == 8):
		return 'Aug'
	if(nMonth == 9):
		return 'Sep'
	if(nMonth == 10):
		return 'Oct'
	if(nMonth == 11):
		return 'Nov'
	if(nMonth == 12):
		return 'Dec'

def strDayName(nDay):
	if(nDay == 1):
		return 'Sunday'
	if(nDay == 2):
		return 'Monday'
	if(nDay == 3):
		return 'Tuesday'
	if(nDay == 4):
		return 'Wednesday'
	if(nDay == 5):
		return 'Thrusday'
	if(nDay == 6):
		return 'Friday'
	if(nDay == 7):
		return 'Saturday'


if __name__ == '__main__':


	nDayNameCounter = 2;

	nMonth = 1;
	nDay = 1;
	nYear = 1900;

	nEndYear = 2001;

	nFirstSundays = 0;

	while(True):
		nDayNameCounter +=1;
		if(nDayNameCounter > 7):
			nDayNameCounter=1;

		nDay += 1;
		if(nDay > daysInMonth(nMonth,nYear)):
			nDay = 1;
			nMonth += 1;
			if(nDayNameCounter == 1 and nYear >= 1901):
				nFirstSundays+=1;

		if(nMonth > 12):
			nMonth = 1;
			nYear+=1;
		if(nYear >= nEndYear):
			break;


		print strDayName(nDayNameCounter) + ': ' + str(nDay) + getMonthString(nMonth) + str(nYear)

	print nFirstSundays


