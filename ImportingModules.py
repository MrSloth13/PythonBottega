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

section_title6 = 'How to Import a Module and Assign an Alias in Python'
section_space6 = f'{section_title6}--------------------------------------------'
print(section_space6)