#!usr/bin/python
#Filename:test1.py
import numpy as np
def readFile(path):
	f = open(path)
	first_ele = True
	for data in f.readlines():
		data = data.strip('\n')
		nums = data.split()
		if(first_ele):
			nums = [float(x) for x in nums]
			matrix = np.array(nums)
			first_ele = False
		else:
			nums = [float(x) for x in nums]
			matrix = np.c_[matrix, nums]
	return matrix
	f.close()
def dealMatrix(matrix):
	print "transpose the matrix"
    	matrix = matrix.transpose()
    	print matrix

    	print "matrix trace "
    	print np.trace(matrix)
#print str.shape
def main():
	matrix = readFile('./hw0_data.dat').transpose()
	column = input('Please input the num of column:')
	#column = int(column)
	#print matrix, '\n', column
	sor = matrix[:, column]
	print sor
	sor.sort()
	print sor
	#print sort
	#print sort.shape
	
if __name__ == '__main__':
	main()
