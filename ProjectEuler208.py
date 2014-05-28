#unsolved :(

import math







if __name__ == '__main__':
	
	fWalkingAngle = (2*math.pi)/5;

	fCurrentFacing = 0;
	vecStartingPosition = [0, 0];

	vecCurrentFacing = [0,0]

	
	vecCurrentPosition = [0, 0];

	nNumberOfJournies = 70;




	for i in range(0,4):

		fCurrentFacing += fWalkingAngle
		vecCurrentFacing[0] = 10*math.cos(fCurrentFacing);

		vecCurrentFacing[1] = 10*math.sin(fCurrentFacing);		
		

		vecCurrentPosition[0]+=int(vecCurrentFacing[0]);
		vecCurrentPosition[1]+=int(vecCurrentFacing[1]);

		print vecCurrentPosition


	for i in range(0,5):

		fCurrentFacing -= fWalkingAngle
		vecCurrentFacing[0] = 10*math.cos(fCurrentFacing);

		vecCurrentFacing[1] = 10*math.sin(fCurrentFacing);		
		

		vecCurrentPosition[0]+=int(vecCurrentFacing[0]);
		vecCurrentPosition[1]+=int(vecCurrentFacing[1]);

		print vecCurrentPosition

	for i in range(0,1):

		fCurrentFacing += fWalkingAngle
		vecCurrentFacing[0] = 10*math.cos(fCurrentFacing);

		vecCurrentFacing[1] = 10*math.sin(fCurrentFacing);
		
		
		vecCurrentPosition[0]+=int(vecCurrentFacing[0]);
		vecCurrentPosition[1]+=int(vecCurrentFacing[1]);

		print vecCurrentPosition


