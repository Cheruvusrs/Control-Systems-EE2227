#!/usr/bin/env python3


import sympy as sp


def SolveAllGains (matrix):
    n = len(matrix)
    matrix = sp.Matrix(matrix)
    identityMatrix = sp.eye(n)
    return (identityMatrix-matrix).inv()


def FinalGain (matrix):
    n = len(matrix)
    finalGain = SolveAllGains(matrix)[0, n-1]
    return str(finalGain), sp.pretty(finalGain, use_unicode=True)


if __name__ == '__main__': #enter the matrix 
    m = [ ['0', '1', '0', '0','0'],#each m(ij) represents direct gain from ith node to jth node
          ['0', '0', 's+1/s', '0','0'],
          ['0', '0', '0', '1','0'],
          ['-1', '0', '0', '0','1/s'],
          ['-1', '0', '0', '0','0'] ]
    print("total gain:") 
    print(FinalGain(m)[1])

	
