import random
import math



def displayMatrix(V):
	for i in range(len(V)):
		for j in range(len(V[0])):
			print(V[i][j],end = " ")
		print()
displayMatrix([[1,2,3],[4,5,6],[7,8,9]])
print()
displayMatrix([[1,2],[5,6],[7,8]])
print()



def getColumns(M):
	Columns = [ [ 0 for i in range(len(M)) ] for j in range(len(M[0])) ]
	for i in range(len(M)):
		for j in range(len(M[0])):
			Columns[j][i] = M[i][j]
	print(Columns)
getColumns([[1,2],[9,7],[7,2]])
print()

def createVectorMatrix(M):
	for i in range(len(M)):
		for j in range(len(M[0])):
			print(M[i][j],end = " ")
		print()
createVectorMatrix([[1,2,3],[4,5,6],[7,8,9]])
print()



def createMatrixRandom(rows,cols,min,max):
	Matrix = []
	for i in range(rows):
		a= []
		for j in range(cols):
			val = random.randint(min,max)
			a.append(val)
		Matrix.append(a)
	for i in range(rows):
		for j in range(cols):
			print(Matrix[i][j],end = " ")
		print()
createMatrixRandom(3,3,1,9)
print()



def addMatrices(M1,M2):
# for rows
	for i in range(len(M1)):
		   # for columns
	   for j in range(len(M1[0])):
	       M1[i][j] = M1[i][j] + M2[i][j]

	for i in range(len(M1)):
		for j in range(len(M1[0])):
			print(M1[i][j],end = " ")
		print()
addMatrices([[1,2,3],[4,5,6],[7,8,9]],[[5,3,3],[3,5,5],[2,2,5]])
print()



def subtractMatrices(M1,M2):
# for rows
	for i in range(len(M1)):
		   # for columns
	   for j in range(len(M1[0])):
	       M1[i][j] = M1[i][j] - M2[i][j]

	for i in range(len(M1)):
		for j in range(len(M1[0])):
			print(M1[i][j],end = " ")
		print()
subtractMatrices([[1,2,3],[4,5,6],[7,8,9]],[[5,3,3],[3,5,5],[2,2,5]])
print()



def multiplyByScalar(M,S):
	Matrix = []
	for i in range(len(M)):
		a = []
		for j in range(len(M[0])):
			val = S * M[i][j]
			a.append(val)
		Matrix.append(a)
	for i in range(len(M)):
		for j in range(len(M[0])):
			print(Matrix[i][j],end = " ")
		print()
multiplyByScalar([[1,2,3],[4,5,6],[7,8,9]],2)
print()


def multiplyMatrices(M1,M2):
# for rows
	for i in range(len(M1)):
		   # for columns
	   for j in range(len(M1[0])):
	       M1[i][j] = M1[i][j] * M2[i][j]

	for i in range(len(M1)):
		for j in range(len(M1[0])):
			print(M1[i][j],end = " ")
		print()
multiplyMatrices([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]])
print()


def powerMatrices(M,S):
	Matrix = []
	for i in range(len(M)):
		a = []
		for j in range(len(M[0])):
			val = M[i][j] ** S
			a.append(val)
		Matrix.append(a)
	for i in range(len(M)):
		for j in range(len(M[0])):
			print(Matrix[i][j],end = " ")
		print()
powerMatrices([[1,2,3],[4,5,6],[7,8,9]],3)
print()



def mainDiagonal(M):
	diagonal = []
	for i in range(len(M)):
		for j in range(len(M[0])):
			if i == j:
				diagonal.append(M[i][j])
	return(diagonal)
print(mainDiagonal([[1,2,3],[4,5,6],[7,8,9]]))
print()


def trace(M):
	trace_M = 0
	diagonal = mainDiagonal(M)
	for i in diagonal:
		trace_M += i
	return trace_M
print(trace([[1,2,3],[4,5,6],[7,8,9]]))
print()



def transposeMatrix(M):
	transpose = [ [ 0 for i in range(len(M)) ] for j in range(len(M[0])) ]
	for i in range(len(M)):
		for j in range(len(M[0])):
			transpose[j][i] = M[i][j]
	for i in range(len(transpose)):
		for j in range(len(transpose[0])):
			print(transpose[i][j],end = " ")
		print()
transposeMatrix([[1,2,3],[4,5,6],[7,8,9]])
print()



def isEqual(M1,M2):
	for i in range(len(M1)):
		for j in range(len(M1[0])):
			if M1[i][j] != M2[i][j]:
				return False
	return True
print(isEqual([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]))
print(isEqual([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[7,6,6],[7,8,9]]))
print()



def isSymmetric(M):
	transpose = [ [ 0 for i in range(len(M)) ] for j in range(len(M[0])) ]
	for i in range(len(M)):
		for j in range(len(M[0])):
			transpose[j][i] = M[i][j]
	for i in range(len(M)):
		for j in range(len(M[0])):
			if transpose[i][j] != M[i][j]:
				return False
	return True
print(isSymmetric([[1,2,3],[4,5,6]]))
print(isSymmetric([[0,3,4],[3,0,7],[4,7,0]]))
print()
