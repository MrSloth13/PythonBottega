section_title1 = 'Python Importing Module Section Introduction'
section_space1 = f'{section_title1}--------------------------------------------'
print(section_space1)

#since this is an introduction it will mostly be just notes. 
"""
So we have done this a tad bit in some of the projects but now it gets its own section in the course. which is well needed. so importing a module is really just importing a library from the 
commmunity that has its own functions built in and ready to use to free up some of your time. you still can build everything out if you wanted to but sometimes its just smarter to use what is
already made instead of constantly trying to remake the wheel. 

Alright so there was a bit more to this then i thought but i was still a bit right. so there are some libaraies like the math one that are still in the main python libarary. you still need to 
import them but don't need to install them. now there are some that have to be installed which i have already done as well though. you need to make a connection to the libarary which is where
PIP comes in. finally i see why this is use. when you do a pip install it is importing the libarary onto the system, and then you can import them into your project like the math function and 
other core python libararies. so i have know about this all along but haven't known why i was doing it. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = 'How to Create a Custom Module and Import It In the Python Repl'
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

#notes
"""
Oh man was this a lesson. i came around in the end but man was it a rough start. so to start i should just say that all of this lesson was in the terminal and i do not have anything to paste 
in here so i will have to try extra hard to explain what learned. so to start i would say if i have to deal with the terminal on my computer i should just use 'git bash'. if i put that in the 
search bar it pops up. the commands are familiar and it just seems to work. once that is open you can move into the folder you want by typing 'cd name of folder' unlike some of the other terminals
you dont need to put in the entire file path. once your in the syntax for making a new folder is 'mkdir name of directory' and the syntax to make a new file is 'touch name of file with.file type'. 
then you can open up the file and work on it in what ever text editor you would like. once its saved you can go back to the terminal and type 'python name of file you want to run.with file type' and 
it will run. now for the whole point of the video is importing custom modules but the thing is, if you make a file of reused fuctions, you can just import that and call the functions like it was any 
other kind of libarary. That is so fucking cool. i can make helper files or my own personal modules and use them on any project that i could need them on. i will leave on, in the terminal if you want 
to import something in python you would type python and it will tell you the version and will put you into a python terminal. from there type 'import name of file with no file type' and bam there you 
go. I imagine that i could just import it in the terminal on here and call import in the file and it will probably work like all the other ones. man that is fucking cool. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title3 = 'How to Import a Custom Python Module into Another File'
section_space3 = f'{section_title3}--------------------------------------------'
print(section_space3)

#notes
"""
Jesus christ this is fucking getting hard as fuck. 

import sys
sys.path.insert(0, './libs')
import helper

def rendering():
    print(helper.greeting('Thomas', 'Nelson'))


rendering()

that is basically what it all boiled down to. if the file you want import is in the same working directory then you can just say 'import name of directory' and it will work. but you will probably want
to store it somewhere way different and that will require more work lol. you will need to follow the first three lines in the example above. do note that i am not sure how detailed you need to make the 
location of the file but will need some experimenting around. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = 'How to Import a Single Function from a Python Module'
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)

#notes
"""
I think that this is going to be like when you use 'import name as name' to import a single function. i think i did something very similar in one of the earlier projects. 


Okay so i was almost right. i had the main concept down but i did not get the syntax right for it. the correct syntax is 'from name import name' pretty simple and i can already see where i got tripped
up but i also think i understand what should be done. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title5 = 'How to Import a Module and Assign an Alias in Python'
section_space5 = f'{section_title5}--------------------------------------------'
print(section_space5)

#notes
"""
Okay so i am almost 100% postive that what i said in the frist place in the lesson above is exactly what we are going to be doing here. 'import name as name' pretting simple. 

and i was right lol. really short and simple video. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title6 = 'How to install PIP on a mac or windows computer'
section_space6 = f'{section_title6}--------------------------------------------'
print(section_space6)

#notes
""" 
So i have definatly messed with pip before but its nice to know the proper way to install pip onto a computer no matter the operating system (was having some trouble getting it on 
a linux distro and was bashing my head in) the next few guide will be going over some of the packages like numpy and stull like that. that is all pip really is, an access line to a 
large network of other modules that could help in your project. 

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title7 = 'Introduction to the Numpy Package in Python'
section_space7 = f'{section_title7}--------------------------------------------'
print(section_space7)

#notes
"""
Okay so i was right when i said i have used numpy before and even importing or downloading i have done before when i had to set up that machine learning program to play flappy bird. and what numpy does
best is work with arrays. now they are not exactly like list in python but are actually more similar to arrays in languages like C# and what not. i will past some of the teminal code we wrote for the 
section below. 

>>> import numpy as np
>>> num_range = np.arange(16)
>>> num_range
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
>>> num_range.reshape(4, 4)
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title8 = 'Overview of the Requests Package in Python to Communicate with APIs'
section_space8 = f'{section_title8}--------------------------------------------'
print(section_space8)

#hell yeah i finally get some knowlage on dealing with API's. this should be a fun and interesting video. 

#notes
"""
Well this went differently then i expected it to. so in python you would communicate with an api with the requests library which means you will need to download and import it. and from what i have seen 
so far you would be well off installing pretty print or pprint as well to help with organizing the json. so in the example we went through the api was layed out in json. which is really just a python 
dictionary that doesn't want to be called one with weird syntax. dont worry too much about json yet since that is not the point in the lesson today. what is important is it works like a dictionary. so 
when you call for a request it will return you json structure but not organize. that you would need pprint.pprint to get it to look right. and navigating works just like navigating through a dictionary 
in python. you can store a certain request or put it in  a list and treat it how you want. i guess the really important thing that i should have probably lead with is to call an api you would use the 
request library followed by the get function in said libarary. it would look like requests.get('link to api'). and yes you need to provide a link to the api to get access to it. and as of right now that
is all i know about api's and communicating with them. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title9 = 'Python Package Section Project Requirement'
section_space9 = f'{section_title9}--------------------------------------------'
print(section_space9)


"""
Okay so i have finished this and im not even going to add the soulution tab to this i am just going to say go look at the files of my solution and jordans. i would 
say to look at jordans first since it is properly built out. mine is very much hard coded and cant be used on any site you put in. my file is 'PythonPackageProd.py'
and jordans is 'JordansPackageScraper.py'. look at them and see all of the things that were useful.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title11 = "Guide to Pipenv for Managing a Python Project's Packages and Environment"
section_space11 = f'{section_title11}--------------------------------------------'
print(section_space11)

"""
I'm going to assume this is a package manager of sorts? I am not sure what else it could be. i do wonder though on weather its more in the terminal or if its like an application. 
"""

#notes
""" 
wow i really almost don't even know where to start. there was so much in that video. so to start i was right about this just being a package manager but he did make sure to explain why they are so important when working on projects. 
to put it shortly, if you are working on a project and you are using, let say numpy for an example, and when you installed it on your system it was at version 1.4. now while you are working on that you get a new commission project
and it will require an older verison on numpy. so you install it and get that project working but when you get back to the first one you will find that it is broken because when you installed the older version you overwrote the 
one you had for the first project. so when you are using pipenv it will keep them separate in an virtual enviorment so when that project needs the dependencys it will be the correct verison. to install pipenv you, givin that you
have python and pip installed, is as simple as pip install pipenv. once you have done that you can install pipenv into any project folder you would like. once you are in a folder you would want to put pipenv in you type 
'pipenv --three' which will create a python 3 project. now what it will make in the directory is a pipfile. if you open it you will see what dependencies are installed in that enviorment. now to install things like numpy or 
request to pipenv is very simple. you would just use pipenv in place of pip. so to install request would be 'pipenv install requests' instead of 'pip install requests' to activate the enviorment type pipenv shell and it will
start. if you type start it will even open a new command promt from the virtual enviorment. that is about it for now but man was that a cool video. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title12 = "Guide to Pipenv for Managing a Python Project's Packages and Environment"
section_space12 = f'{section_title12}--------------------------------------------'
print(section_space12)