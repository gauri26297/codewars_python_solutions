'''
https://www.codewars.com/kata/5324945e2ece5e1f32000370

Description:

Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
'''

def sum_strings(x, y):
    a, b = len(x), len(y)
    m = max(a,b)
    x = x.zfill(m)
    y = y.zfill(m)
    op = ''
    carry = 0
    for i in range(m-1,-1,-1):
        carry, op_digit = divmod(int(x[i])+int(y[i])+carry, 10)
        op += str(op_digit)
    
    return ('1'*carry + op[::-1]).lstrip('0') or '0'

print("sum_strings('1','2') = ",sum_strings('1','2'))