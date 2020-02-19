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
    for num in range(1,21):
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

"""
Before i start the video i wanted to try and guess the answer myself. i would assume what it means to return a value from a function is to have it give you something back. as in
if you are performing a calculation you would want the end result of the inputs and proccess to be what is returned seeing as you wouldn't really care about all the rest of it if 
you just need the result of the calculation. could be totally wrong here but just wanted to guess to see how right i am. 
"""

def full_name2(first, last):
    return f'{first} {last}'


jon = full_name2('jon', 'Billingfort')

print(jon)


#notes
"""
So i was right i suppose. the real point of the video was to explain the difference between using the print statement vs the return statment in a function and why you wont really (or should) 
use the print statment unless you are debugging in the real world. when you call a print statment the only place that it goes in to the console which isn't very useful in a normal program. but
if you use the return statment, nothing will show in the console but the value you called to be returned will be passed onto any other function or method that needs it. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = 'How to Nest Functions in Parent Functions in Python'
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)

# this should be a good video. i understand how to nest functions in a function but the parent call out makes me think that i don't know it all though. 

def greeting(first, last):
    def full_name3():
        return f'{first} {last}'

    print(f'Hi {full_name3()}!')


greeting('John', 'Jimmy')

#notes
"""
This was interesting but there isnt anything i was really missing. i did have some trouble getting the code to work but i can see where i was messing up now. i need to make sure i have all the right things indented
correctly, especially when nesting functions due to local variable scope in python. another thing i learned is that python is one of the few languages that even allow for a function to be nested. and as far as when
to nest vs when to keep functions separate, jordan had a good rule of thumb. if the only time you will use the function is inside or to serivce a parent fucntion then it is probably best to nest the function in the 
parent one. otherwise keeping them separate is the better way to go. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title5 = 'Guide to Default Arguments in Python Functions'
section_space5 = f'{section_title5}--------------------------------------------'
print(section_space5)

def greeting2(name = 'Guest'):
    print(f'Hi {name}')


#greeting2() this will result in an error since it needs an argument. 
greeting2('Kristine')
greeting2()

#some things to not do. 

def some_function(colletion = []):
    colletion.append(1)
    return colletion

print(some_function())

print(some_function())

#notes
"""
This is a very interesting topic. So to start a default argument in a function is what an argument should be, if there is nothing provided. this way your program can be more dynamic in how it functions. to do so all you 
need to do is call your argument, and = what you want it to be. its that simple. jordan did go over what to watch out for and this is where it gets interesting. one thing you never want to do is have a default argument be
a muteable variable. meaning you dont want it to be able to be changed. especially list. this is because any action done to the default argument will carry on the enitre time. you want to use an ummutable variable so it 
cannot actually be changed, just reassined which can then be used in its own separate instance. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title6 = 'How to Utilize Named Function Arguments in Python'
section_space6 = f'{section_title6}--------------------------------------------'
print(section_space6)

def full_name4(last, first):
    print(f'{first} {last}')


full_name4(first = 'Kristine', last = 'Hudgens')

#so far all we have used for arguments is positional meaning the variables we put in are being mapped based off order. 

#notes
"""
So this is interesting. so the way you can get around the positional mapping is when you call the function and actually pass in the arguments you can just put the name of the arugment that you want to pass and set 
it equal to the argument you want it to be. i have an example above if that is confsuing. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title7 = 'Guide to Function Argument Unpacking in Python'
section_space7 = f'{section_title7}--------------------------------------------'
print(section_space7)