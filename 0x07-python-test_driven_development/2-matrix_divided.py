#!/usr/bin/python3
"""Definesadividefnforamatrix"""
defmatrix_divided(matrix,div):
"""Dividesallmatrixelements.

Args:
matrix(list):(listoflists)ofintegers/floats
div(int/float):divisionsign

Raises:
TypeError:Ifnotanint
TypeError:ifmatricesareofdifferentsizes
TypeError:ifdiv!=int/float
ZeroDivisionError:ifdiv=0

Return:
divisionresultinamatrix
"""
if(notisinstance(matrix,list)ormatrix==[]ornotall((isinstance(ele,int)
orisinstance(ele,float))forelein[numforrowinmatrixfornuminrow])):
raiseTypeError("matrixmustbeamatrix(listoflists)of""integers/floats")
ifnotall(len(row)==len(matrix[0])forrowinmatrix):
raiseTypeError("Eachrowofthematrixmusthavethesamesize")
ifnotisinstance(div,int)andnotisinstance(div,float):
raiseTypeError("divmustbeanumber")
ifdiv==0:
raiseZeroDivisionError("divisionbyzero")
return([list(map(lambdax:round(x/div,2),row))forrowinmatrix])
