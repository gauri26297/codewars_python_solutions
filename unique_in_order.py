'''
https://www.codewars.com/kata/54e6533c92449cc251001667

Description:

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
'''

def unique_in_order(iterable):
    iterable_ = iter(iterable)
    try :
        last_itr = next(iterable_)
    except StopIteration :
        return []
    list1 = [last_itr]
    for itr in iterable_:
        if itr != last_itr:
            list1.append(itr)
            last_itr = itr
    return list1


print("unique_in_order('AAAABBBCCDAABBB') == ",unique_in_order('AAAABBBCCDAABBB'))
print("unique_in_order('ABBCcAD')         == ",unique_in_order('ABBCcAD'))
print("unique_in_order([1, 2, 2, 3, 3])   == ",unique_in_order([1, 2, 2, 3, 3]))
print("unique_in_order((1, 2, 2, 3, 3))   == ",unique_in_order((1, 2, 2, 3, 3)))