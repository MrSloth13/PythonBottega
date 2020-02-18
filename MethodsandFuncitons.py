section_title1 = 'Python Methods and Functions Section Introduction'
section_space1 = f'{section_title1}--------------------------------------------'
print(section_space1)

#new section!!

"""
a methon or function can store instructions and proccesses you can call back at 
a latter time. there is the inuput, the function itself, and the return of what 
you want back. so its nice to be able have a funciton that you can call when you
need it and if there is a change to be made you can just change the original 
function and it should update everywhere else as well. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = 'Basic Syntax for Creating Python Functions'
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

# well i think i already know a decent bit on this as far as the basics are concerned. 

def full_name(first, last):
    print(f'{first} {last}')


full_name('Thomas', 'Nelson')


def auth(email, password):
    if email == 'jelly@email.com' and password == 'secret':
        print('You are authorized')
    else:
        print('You are NOT authorized')


auth('jelly@email.com', 'secret')


def hundred():
    for num in range(1,101):
        print(num)

hundred()


#notes
"""
This was a very good refresher on functions in python. i did remember most of the syntax to start with. like how you need to start with 'def' and end the first line like a conditional, with 
a ':' at the end. then make sure everything you want in that funciton is in a code block (indented). you also have your arguments that you can set to have things passed through or not depending
on how you built out your function. the naming convention for best practices is the exact same as if you were creating a variable in python. other then that i feel like i have a good grasp on 
basic functions on python. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title3 = 'What Does it Mean to Return a Value from a Python Function?'
section_space3 = f'{section_title3}--------------------------------------------'
print(section_space3)