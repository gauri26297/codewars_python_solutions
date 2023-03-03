'''
https://www.codewars.com/kata/5467e4d82edf8bbf40000155

Description:

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
Examples:

Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

'''

def descending_order(num):
    num=[int(i) for i in list(str(num))]
    ret='0'
    while len(num)>0:
        m=max(num)
        ret=ret+str(m)
        num.remove(m)
    return int(ret)

print('Input: 42145 Output: ', descending_order(54421))

print('Input: 145263 Output: ', descending_order(654321))

print('Input: 123456789 Output: ',descending_order(987654321))