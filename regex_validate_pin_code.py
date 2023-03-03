'''
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

Description:

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

'''

def validate_pin(pin):
    op = True
    if len(pin)==4 or len(pin)==6:
        try: 
            for idx in range(len(pin)):
                op = op and float(pin[idx])%1==0
            return op
        except:
            return False
    else:
        return False
    
print('"1234"   -->  ',validate_pin('1234'))
print('"12345"   -->  ',validate_pin('12345'))
print('"a234"   -->  ',validate_pin('a234'))