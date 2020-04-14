#Code by C.Sri Ram Saran
#April 13th ,2020
#Released under GNU GPL
#!/usr/bin/env python3
#this code uses the matrix equivalence form of masons gain formula.


import sympy as sp
import numpy as np

s=sp.Symbol('s')# creates 's' as symbol variable
def SolveAllGains (matrix):# function to generate a matrix whose element aij contains total gain between ith node to jth node
    n = len(matrix)# length of transition matrix
    Matrix=sp.Matrix(matrix)# converting a list 'matrix' into a sympy Matrix
    identityMatrix = sp.eye(n)# a identity matrix is created using sp.eye()
    return (identityMatrix-Matrix)**-1# returns the inverse of (identityMatrix-Matrix)


def FinalGain (matrix):# function which returns the total gain between ith node and jth node
    n = len(matrix)# length of transition matrix
    finalGain = SolveAllGains(matrix)[0, n-1]# here total gain between ith and jth node is found ,here i=0,j=n-1
    return (finalGain)# returns the total gain between ith and jth node


 #enter the matrix 
m = [ [0, 1, 0, 0,0],#enter the transition matrix here,each element of m- m(ij) represents direct branch gain from ith node to jth node
[0, 0, s+1/s, 0,0],
[0, 0, 0, 1,0],
[-1, 0, 0, 0,1/s],
[-1, 0, 0, 0,0] ]
print("total gain:") 
print(sp.cancel(sp.simplify(FinalGain(m))))
