'''
https://www.codewars.com/kata/520446778469526ec0000001

Description:

Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

'''


import numpy as np
def same_structure_as(original,other):
    op = True and (type(original) == type(other)) and (len(original)==len(other))
    for itr in range(len(original)):
        op = op and np.shape(original[itr]) == np.shape(other[itr])
    return op


# should return True
print("same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )"," : ",same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
print("same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )"," : ",same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ))

# should return False 
print("same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )"," : ",same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
print("same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )"," : ",same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ))

# should return True
print("same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )"," : ",same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))

# should return False
print("same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )"," : ",same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ))