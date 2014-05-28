import math
if __name__ == '__main__':
	
	
	for a in range(11,1000):
		
		aSquared = a*a;
		#print a
		for b in range(a+1,1000):
			bSquared = b*b;
			c = math.sqrt(aSquared + bSquared)
			if(a+b+c == 1000):
				print "a:" + str(a) + " b:" + str(b)+ " c:" + str(c)
				print int(a*b*c)
				break;
		