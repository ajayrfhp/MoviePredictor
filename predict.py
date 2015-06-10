import sys

import numpy
import random
from sklearn import linear_model
from sklearn import svm
from glb import *
from functions import *
from model import *

inputData=[]

movieNameList=sys.argv[1:]
movieName=""
for name in movieNameList:
	movieName=movieName+name+" "
print movieName	
cnt=0
m={0:0,1:0,2:0,3:0}

#### DATA CLEANING 
#inputFeature=[1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 6.9, 12.2455, 10.0, 4.5, 1.2857156857142857, 6.422812729725015, 6.976923076923077, 12.2455, 10.0, 5.8, 1.2857156857142857, 7.081025974320272]
inputFeature=getFingerPrint(movieName)

line=inputFeature
	
for l in range(len(line)):
	if(l==22):
		continue
	
	elif(line[l]!=''):
		line[l]=float(line[l])
		inputData.append(line[l])





clf=constructModel()






prediction=int(clf.predict(inputData))

#clf=svm.SVC()
if(prediction==0):
	print "BLOCKBUSTER"
elif(prediction==1):
	print "CRITICAL WINNER"	
elif(prediction==2):
	print "COMMERCIAL VENTURE"
else:
	print "MEDIOCORE	"	
###TEST

