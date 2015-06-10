import numpy
import random
from sklearn import linear_model
from sklearn import svm



m={0:0,1:0,2:0,3:0}
def constructModel():
	inputData=[]
	targetData=[]
	trainingData=[]
	trainingTarget=[]
	testData=[]
	testTarget=[]
	cnt=0
#### DATA CLEANING 
	with open('data.txt','r') as f:
		for line in f:
			line=line.rstrip().split(",")
			cnt+=1
			subData=[]
			subTarget=[]

			if(int(line[33]))>3:
				line[33]=3
			m[int(line[33])]+=1
			
			for l in range(len(line)):
				if(l==22):
					continue
				
				if(l+2==len(line)):
					line[l]=float(line[l])
					targetData.append(line[l])
				elif(line[l]!=''):
					line[l]=float(line[l])
					subData.append(line[l])
			inputData.append(subData)


	indices=random.sample([i for i in range(len(inputData))],100)

	###DATA CLEANING DONE DIVIDING DATASET INTO TEST AND TRAINING DATA
	for i in range(len(inputData)):
		if i not in indices:
			trainingData.append(inputData[i])
		else:
			testData.append(inputData[i])	
	for i in range(len(targetData)):
		if i not in indices:
			trainingTarget.append(targetData[i])
		else:
			testTarget.append(targetData[i])




	####DIVIDED INTO TRAINING DATA AND TEST DATA 
	'''''DATA PREPARING AND CLEANING STEPS 
	HERE COMES THE MODEL '''
	cnt=0
	
	clf=svm.SVC()
	clf.fit(trainingData,trainingTarget)
	for i in range(len(testData)):
		if(int(clf.predict(testData[i]))==testTarget[i]):
			cnt+=1
		
	###TEST
	print cnt
	return clf
constructModel()	