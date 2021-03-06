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

def full_name5(first, last):
    print((f'{first} {last}'))


full_name5('John' ,'Adams')

def greeting3(*args):
    print("Hi " + " ".join(args))


greeting3('Billy', 'jean' , 'Noel')

#notes
"""
This is such a nice thing and i can already see it being one of the most important ones i have learned so far. so i would say the biggest two take aways from the video is that 'args' is the best practice
name for when you use an unpacking method of using arguments. the next, and more important, is that when you pass is the arguments they will be treated as tuples. so this means when you call them in the 
function itself you have to use tuple funcitons and methods or convert it to a list for more flexability. i would say that this is one of the best things i have seen about python so far. the fact that you can 
take in as many arguments as you want and interact with them, loop over them, and treat a large group of arguments like a collection. it also makes it much more of a flexable function at the same time. any
machine learning program is forsure going to use this because you might not be to sure how many arguments will be paseed into the function when it is called. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title8 = 'Overview of Keyword Arguments in Python Functions'
section_space8 = f'{section_title8}--------------------------------------------'
print(section_space8)

def greeting4(**kwargs):
    if kwargs:
        print(f'Hi {kwargs["first_name"]} {kwargs["last_name"]}, I hope your having a wonderful day!')
    else:
        print('Please either sign in or create an account')


greeting4(first_name = 'Bobby', last_name = 'Martain')
greeting4()

#notes
"""
This was cool. so this is a further dive into the same topic as before but expands it a bit. this time we are working with keyword arguments. which is when you are assigning where an argument it mapped
when you pass it in. if you want to use that when you call the function you would use a bit similar syntax but it DOES NOT use a TUPLE. so the syntax that you would put in the function is **kwargs which 
shows you the syntax and the best practice name for it. now if you are like me when you heard 'keyword' in the title you thought i bet it works or uses dictionaries instead of tuple and you would be correct.
unlike the normal argument unpacking this will have to be worked with like a dictionary with all of its related functions. or like i said above, separate the keys from the values and convert to a list while
separating if you need more flexability. and you would use the same syntax in the function when you call it. so if you called the function 'greeting77()' you would still use the same keyword assignment as you
would any other time. 'greeting77(first_name = 'Thomas', last_name = 'Nelson'). and the function will use the keyword as the key for the dictionary (duh), and use the value for the value for the occociated key
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title9 = 'How to Combine All Argument Types in a Single Python Function'
section_space9 = f'{section_title9}--------------------------------------------'
print(section_space9)

def greeting5(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope that you are having a great {time_of_day}")

    if kwargs:
        print('Your task for the day are:')
        for key, val in kwargs.items():
            print(f"{key} => {val}")


greeting5('Morning',
        'kristine', 'Hudgens',
        first = 'Empty Dishwasher',
        second = 'Take the dog outside',
        third = 'Homework')

#notes
"""
Okay so i think i am getting the hang of this now that we are using all of them together. i can see how each can work with eachother but also what they are best at compared to the other ways. over all i think that i 
feel confident in my knowlege on this so far. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title10 = 'Guide to Python Lambdas'
section_space10 = f'{section_title10}--------------------------------------------'
print(section_space10)

#this is going to be interesting. mainly since i used a lambda in the reduce function and really didn't know how it worked.

#lamba def
"""
a lambda is a function, that is usally a small one, that can be passed into other functions. this allows you to treat it like a variable but instead of having a string or a number stored you have a proccess or 
some exicutabe code.
"""

full_name7 = lambda first, last: f'{first} {last}'

print(full_name7('Thomas', 'Nelson'))

def greeting6(name):
    print(f'Hi there {name}')


greeting6(full_name7('John', 'betty'))

#notes
"""
Wow this all makes sense now when put in the context of the dynamic reduce function from a while back. so the syntax for it is ' lambda argument_name, argument_name: what you want the function to do '. now this is 
normally stored in a variable but it some functions like the reduce function require a lambda to be passed into it. you can then call that variable that you stored the lambda in and pass in the arguments for it and
it will all work as you'd expect. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title11 = 'Project Requirements: Build FizzBuzz in Python'
section_space11 = f'{section_title11}--------------------------------------------'
print(section_space11)

#Oh boy here we go lol.

"""
Write a program that prints the numbers from 1 to 100
But for miltiples of three print "Fizz" instead of the 
number and for the multiples of five print "Buzz". For
numbers which are muliples of both three and five print
"FizzBuzz".
"""

# a multiple of 3 is any number that is multipled by 3.
# a mulitple of 5 is any number that is multipled by 5.


def fizz_buzz(max_value):
    max_value += 1

    multiple_of_three_check = lambda a: a % 3
    multiple_of_five_check = lambda a: a % 5

    for num in range(1, max_value):
        if multiple_of_three_check(num) == 0 and multiple_of_five_check(num) == 0:
            print('FizzBuzz')
        elif multiple_of_three_check(num) == 0:
            print('Fizz')
        elif multiple_of_five_check(num) == 0:
            print('Buzz')
        else:
            print(num)



fizz_buzz(100)

#notes
"""
So this went so much better then i expected. i was able to get it done in under 20 minutes and i even got a compliment on using lambda to get the solution that was required. i was expecting this
to go very long but got it done in no time and i feel like i have a grasp on things. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title12 = 'Solution to FizzBuzz in Python'
section_space12 = f'{section_title12}--------------------------------------------'
print(section_space12)

#Jordans Soulution
def jfizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


jfizz_buzz(100)

#notes
"""
I like how he did it a bit more then the way i did. i could have not used lambda and not reassigned the max value. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#i think that is it for the methods and the conditional section of the course for python. onto module section's!