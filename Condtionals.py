section_title1 = "Introduction to Python Conditionals"
section_space1 = f'{section_title1}--------------------------------------------'
print(section_space1)

#we are onto condtionals now!! whooooo!!!!

#notes
"""
this is one of the most important things in programming. all it really is, is a way to check to see if a senario is true, then exicute specific code for it. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = 'Overview of Python Conditionals'
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

age = 25

if age == 25:
    print('Supeeerrr')
elif age > 100:
    print('you too old my guy')
else:
    print('noooppe')

#notes
"""
so this was mostly just review for me but i did not know about the else if conditional. so you spell it like elif for else if and then you put a normal conditional check syntax then 
close it off with : unlike the else where you put the : right after else. it a good way to add another conditional or a nested on after a first conditional. pretty cool.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title3 = 'How to Use the Ternary Operator in Python Conditionals'
section_space3 = f'{section_title3}--------------------------------------------'
print(section_space3)

role = 'admin'

auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)

passoword_for_pillow_fort = 'peanuts'

whats_the_password = 'That is the password, come in' if passoword_for_pillow_fort == 'peanuts' else 'You are not allowed'

print(whats_the_password)

#notes
"""
Okay so this is sweet but jordan did offer some caution when making these since they do add complexity and can make it harder to read but definalty have there place. So you would use this when you want to assign things
with a conditional. and all it really does is remaps a normal if else conditional. you would name the variable and assign it (=), then put what you want to happen if the condition is true, then put your if statement
like if 2 == 2, then you put else, then what you would want to happen if the conditional is not met. simple but i can see how it can be hard to read. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = 'Full List of Python Conditional Operators'
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)