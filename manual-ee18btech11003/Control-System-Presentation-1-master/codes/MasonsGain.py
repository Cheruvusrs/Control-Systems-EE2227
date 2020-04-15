#Code by C.Sri Ram Saran
#April 13th ,2020
#Released under GNU GPL
#!/usr/bin/env python3


import sympy as sp
import numpy as np

s=sp.Symbol('s')# creates 's' as symbol variable
def SolveAllGains (matrix):# function to generate a matrix whose element aij contains total gain between jth node to ith node
    n = len(matrix)# length of transition matrix
    Matrix=sp.Matrix(matrix)# converting a list 'matrix' into a sympy Matrix
    identityMatrix = sp.eye(n)# a identity matrix is created using sp.eye()
    return (identityMatrix-Matrix)**-1# returns the inverse of (identityMatrix-Matrix)


def FinalGain (matrix):# function which returns the total gain from jth node to ith node
    n = len(matrix)# length of transition matrix
    finalGain = SolveAllGains(matrix)[n-1, 0]# here total gain between ith and jth node is found ,here i=n-1,j=0
    return (finalGain)# returns the total gain from jth to ith node


 #enter the matrix 
m = [ [0, 0, 0, -1,-1],#enter the transition matrix here,each element of m- m(ij) represents direct branch gain from jth node to ith node
[1, 0, 0, 0,0],
[0, s+1/s, 0, 0,0],
[0, 0, 1, 0,0],
[0, 0, 0, 1/s,0] ]
print("total gain:") 
print(sp.cancel(sp.simplify(FinalGain(m))))
