'''
https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

Description:

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''

def max_sequence(arr):
    #make the array an iterable (it is still same as arr but will work with next() and as iterable in for loop)
    iter_arr = iter(arr)
    try:
        #temp sum is initialized by the first entry
        temp_sum = next(iter_arr)
    except StopIteration: # means the array is empty
        temp_sum = 0 # the sum is initialized by 0
    #max sum is initialized by the temp sum above
    max_sum = temp_sum
    #iterate through the array only once (one entry is already exhausted by next())
    for int_ in iter_arr:
        #update the known temperory sum by adding current int to it
        temp_sum += int_
        #is updated sum less than the int? 
        if int_ > temp_sum:
            #this means our new sublist will start from this integer
            temp_sum = int_
        #is updated temp_sum greater than the max sum of all times?
        if temp_sum > max_sum:
            #update max_sum
            max_sum = temp_sum
    return max_sum if max_sum > 0 else 0 #0 for empty or negative list

print('max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) gives : ',max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))