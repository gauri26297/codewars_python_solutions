'''
https://www.codewars.com/kata/544aed4c4a30184e960010f4

Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''

def divisors(integer):
    d=[]
    for n in range(integer-2):
        if integer%(n+2)==0:
            d.append(n+2)

    if len(d)==0:
        return (str(integer)+' is prime')
    else:
        return d
    

print('divisors(12) : ',divisors(12))
print('divisors(25) : ',divisors(25))
print('divisors(13) : ',divisors(13))