'''
https://www.codewars.com/kata/526dbd6c8c0eb53254000110

Description:

In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

    At least one character ("" is not valid)
    Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
    No whitespaces / underscore

'''

def alphanumeric(password):
    return password.isalnum()
    '''if password:
        alphanum = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        for ch in password:
            if (ch in [" ", "_"]) or (ch.lower() not in alphanum):
                return False
        return True
    else:
        return False'''

print(alphanumeric('Sup3rman'))