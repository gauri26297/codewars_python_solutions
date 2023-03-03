'''
https://www.codewars.com/kata/55c04b4cc56a697bb0000048

Description:

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered.

Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

'''

def scramble(s1, s2):
    list1 = []
    for ch in s2:
        if ch not in list1:
            list1.append(ch)
            if s2.count(ch) > s1.count(ch):
                return False        
    return True

print("scramble('rkqodlw', 'world')",scramble('rkqodlw', 'world'))
print("scramble('cedewaraaossoqqyt', 'codewars')",scramble('cedewaraaossoqqyt', 'codewars'))
print("scramble('katas', 'steak')",scramble('katas', 'steak'))