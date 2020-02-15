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

#what he means by operator is what you can put in a conditional to check values. 

# List of comparision operators
# == Equality
# != Inequality
# <> Inequality (deprecated) this is no longer used and has been replaced by != so just know if you run into this looking at someone else's code you can know what it is. 
# > Greater than
# >= Greater then or equal to
# < Less than
# <= Less than or equal to

username = 'jonsnow'

if username != 'jonsnow':
    print('welcome!')
else:
    print('You shall not pass')


user_list = ['Kristine', 'Tiffany']
second_list = ['Jordan', 'Braydan']

if user_list == second_list:
    print('They match!')
else:
    print('These are very different sir')
    

#notes
"""
So this was nice. i knew most of them since they are identical to C# operators. the one differnce is in C# you could not perform a > or < on a string. it would throw an error since it is much more strict as far
as its data type mingling i guess you could say. still a good video though. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title5 = 'How to Check if a Value is Included in a Python String or List'
section_space5 = f'{section_title5}--------------------------------------------'
print(section_space5)

#conditionals in python also can check to see if a value is in a string or list. 

sentence = 'The quick brown fox jumped over the lazy Dog'

word = 'dog'

if word.lower() in sentence.lower():
    print('The word was found in the sentence')
else:
    print('The word was not found in the sentence')

nums = [1, 2, 3, 4]

if 3 in nums:
    print('The number was found')
else:
    print('The number was not found')

#notes
"""
This is really cool and is not something that i have experience with in C#. and i also like the way it reads. its very literal. so the way it works is simple and kinda a loop conditional hybrid syntax. you would start with
if then what you want to check is in the string or list, then put 'in' and then the string or list you want to check. then put the : at the end and put in your code block. and since this is a conditional you can still use the 
else statements and everything that you would normally do when working with conditionals. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title6 = 'How to Build Compound Conditionals in Python'
section_space6 = f'{section_title6}--------------------------------------------'
print(section_space6)