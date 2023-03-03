'''
https://www.codewars.com/kata/52774a314c2333f0a7000688

Description:

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

'''

def valid_parentheses(string):
    #initialize count
    count = 0
    
    #for all the characters in the sting,
    for ch in string :
        #if character is open bracket, increase the count
        if ch == "(":
            count += 1
        #if character is close bracket, decrease the count
        elif ch == ")":
            count -= 1
            #count should be positive in a valid string while calculating
            if count < 0:
                return False
    #final count should be zero in a valid string
    if count != 0:
        return False
    else :
        return True


print('"()"              =>  ',valid_parentheses("()"))
print('")(()))"          =>  ',valid_parentheses(")(()))"))
print('"("               =>  ',valid_parentheses("("))
print('"(())((()())())"  =>  ',valid_parentheses("(())((()())())"))