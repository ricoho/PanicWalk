from random import randrange
from math import atan,cos,sin
import numpy as np
TotalT=10
delT=1
TimeStep = (TotalT)/(delT)
ForceConstant = 1
Constant = 1
delTseq=(delT^2)
def randpartgen(PartNumber,BoxSize):
	global PartMat
	PartMat=[[0 for i in range (2)] for j in range (PartNumber)]
	for i in range (PartNumber):
		PartMat[i][0]=randrange(0,BoxSize,1)
		PartMat[i][1]=randrange(0,BoxSize,1)
			 
	return PartMat
	
randpartgen(10,100)
f_handle = file('test.txt', 'a')
print PartMat
newPartMat= np.reshape(PartMat,20)
print "the new one is:", newPartMat
np.savetxt(f_handle,newPartMat,delimiter=',',newline=' ',fmt='%s')