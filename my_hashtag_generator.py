'''
https://www.codewars.com/kata/52449b062fb80683ec000024/solutions/python

Description:

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

'''

def generate_hashtag(s):
    if s:
        list1 = s.split()
        op = '#'
        for ch in list1:
            op = op + ch.title()
        if len(op) > 140:
            return False
        return op
    else:
        return False

print(" Hello there thanks for trying my Kata" , "......", generate_hashtag(" Hello there thanks for trying my Kata"))
print("    Hello     World   ", "......",  generate_hashtag("    Hello     World   "))
print("",  "......", generate_hashtag(""))