from random import randrange
from math import atan,cos,sin
TimeStep = (TotalT)/(delT)
ForceConstant = 1
Constant = 1
delTseq=(delT^2)
#This function is used to generate the coordinate of those particle at t=0#
def randpartgen(PartNumber,BoxSize):
	global PartMat
	PartMat=[[0 for i in range (2)] for j in range (PartNumber)]
#PartMat is a 2D array consisting of all the coordinates of particle at t=0# 
	for i in range (PartNumber):
		PartMat[i][0]=randrange(0,BoxSize,1)
		PartMat[i][1]=randrange(0,BoxSize,1)
			 
	return PartMat
	
def writefile(array):
	f_handle = file('dataoutput.txt', 'a')
	newPartMat= np.reshape(array,20)
	np.savetxt(f_handle,newPartMat,delimiter=',',newline=' ',fmt='%s')
	
	
def MolDynamics(delT,TotalT):
#We use Verlet MD to calculate the position of particle at t not equal to 0
	NewPartMat=PartMat=[[0 for i in range (2)] for j in range (PartNumber)]
	for time in range (2,TimeStep):
		Ptime=time-1
		for PartNo in range (1, PartNumber):
			PartMat[0][PartNo]= PartX
			PartMat[1][PartNo]= PartY
			
			#Calculate the force acted on the Particle#
			#
			Distance= sqrt((BoxSize-PartX)^2+(BoxSize/2.0 - PartY)^2)
			MagOfForce = Distance * ForceConstant + Constant
			ForceX= MagofForce * cos(atan( (BoxSize/2.0 - PartY)/ (BoxSize-PartX)))
			ForceY= MagofForce * sin(atan( (BoxSize/2.0 - PartY)/ (BoxSize-PartX)))
			##
			
			if time = 2:
				dx= floor(0.5*ForceX*(delTseq))
				dx= floor(0.5*ForceX*(delTseq))
				
				PartX = PartX + dx
				PartY = PartY + dy

			else:
			#this is the verlet algorithm
				PartX=2*NewPartMat[0][PartNo]-PartMat[0][PartNo]+ForceX*(delTseq)
				PartY=2*NewPartMat[1][PartNo]-PartMat[1][PartNo]+ForceY*(delTseq)
				
			NewPartMat[0][PartNo]= PartX
			NewPartMat[1][PartNo]= PartY
			writefile(NewPartMat)
				
