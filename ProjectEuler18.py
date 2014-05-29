


class pyramidNode:
	def __init__(self,value,row,column):
		self.value = value;
		self.nRow = row;
		self.nColumn = column
		self.weight = value


if __name__ == '__main__':

	pyramidRows=[];
	pyramidFile = open('ProjectEuler18_pyramid.txt');
	nRow = -1;
	for line in pyramidFile:
		nRow +=1;
		nColumn = -1;
		pyramidValues = [];
		for num in line.split(' '):
			nColumn +=1;
			pyramidValues.append(pyramidNode(int(num),nRow,nColumn));
		pyramidRows.append(pyramidValues);




	for i in range(0,pyramidRows.__len__()-1):
		
		for node in pyramidRows[i]:
			childLeft = pyramidRows[i+1][node.nColumn]
			childRight = pyramidRows[i+1][node.nColumn+1]
			if(childLeft.weight < childLeft.value+node.weight):
				childLeft.weight = childLeft.value+node.weight;
			if(childRight.weight < childRight.value+node.weight):
				childRight.weight = childRight.value+node.weight;


	for i in range(0,pyramidRows.__len__()):
		string = '';		
		for node in pyramidRows[i]:
			string += ' ' + str(node.value)+':' + str(node.weight)
		print string


	curNode=None;
	for node in pyramidRows[pyramidRows.__len__()-1]:
		if curNode == None:
			curNode = node;
		elif curNode.weight < node.weight:
			curNode = node;

	print curNode.weight