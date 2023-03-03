'''
https://www.codewars.com/kata/54da5a58ea159efa38000836

Description:

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
Examples

[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''

def find_it(seq):
    '''Find unique integers in the given sequence'''
    uniq = []
    for itr in seq:
        if not (itr in uniq):
            uniq.append(itr)
    
    '''see how many times each of the unique integers occured'''
    counts = [0]*len(uniq)
    for int_ in seq:
        counts[uniq.index(int_)] += 1

    '''find the index of integer that occured odd number of times'''
    idx = 0
    for itr in counts:
        if itr % 2 == 1:
            return uniq[idx]
        idx += 1

print('[7] returns : ', find_it([7]))
print('[0] returns : ', find_it([0]))
print('[1,1,2] returns : ', find_it([1,1,2]))
print('[0,1,0,1,0] returns : ', find_it([0,1,0,1,0]))
print('[1,2,2,3,3,3,4,3,3,3,2,2,1] returns : ', find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))