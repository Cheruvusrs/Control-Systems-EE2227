#Code by C.Sri Ram Saran
#April 13th ,2020
#Released under GNU GPL
#!/usr/bin/env python3


import sympy as sp


def SolveAllGains (matrix):# function to generate a matrix whose element aij contains total gain between ith node to jth node
    n = len(matrix)
    matrix = sp.Matrix(matrix)
    identityMatrix = sp.eye(n)
    return (identityMatrix-matrix).inv()


def FinalGain (matrix):#returns the total gain between ith node and jth node
    n = len(matrix)
    finalGain = SolveAllGains(matrix)[0, n-1]# here gain between ith and jth node is found ,here i=0,j=n-1
    return str(finalGain), sp.pretty(finalGain, use_unicode=True)


if __name__ == '__main__': #enter the matrix 
    m = [ ['0', '1', '0', '0','0'],#each m(ij) represents direct branch gain from ith node to jth node
          ['0', '0', 's+1/s', '0','0'],
          ['0', '0', '0', '1','0'],
          ['-1', '0', '0', '0','1/s'],
          ['-1', '0', '0', '0','0'] ]
    print("total gain:") 
    print(FinalGain(m)[1])
