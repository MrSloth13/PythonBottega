#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title1 = "How to Create and Write to a File in Python"
section_space1 = f'{section_title1}--------------------------------------------'
print(section_space1)

file_builder = open('logger.txt', 'w+')

for i in range(100):
    file_builder.write(f'Im on line {i + 1}\n')

#file_builder.write('Hey, Im in a file')

file_builder.close()

#notes
"""
This is really fucking cool lol. i finally feel like i am making something or learning what i need 
to actually make something. so to start if you want to open a file you would use assignment and use
the 'open()' function within python itself. now that takes two string arguments which are and name
of the file and what permissions you want to allow. i dont know all the permissions but i do now 
know that 'w+' means im allowed to write to the file. one important note is that the open function 
look through the folder to see if it can find any file with that name, if it does not however it 
will create that file for you. so you would use open to open and create files. now he also went over
the write function which you would just call like .write() and put what you want to write to file. 
jordan did warn though that using this syntax by just opening and writing a file will just completly 
re-write the file. the entire thing. so i would only recommend using this exact syntax when working 
with new file and not an existing one. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = "Using Regular Expressions to List File Types in Python"
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

"""
to start we are not going to go crazy with what regular expressions are in detail but know that
they are used to see patterns. so dont worry if you dont fully understand what a regular expression 
is or isnt yet. there is an entire section later in the course on what they do. 
"""

"""
import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('text files:', file)

        if fnmatch.fnmatch(file, '*.rb'):
            print('ruby files:', file)

# list_files()


players = [
    'Jose Altuve 2B',
    'Carlos Correa SS',
    'Alex Bregman 3B',
    'Scooter Gennet 2B'
]

second_base_players = [player for player in players if fnmatchcase(player, "*2B")]

print(second_base_players)
print('players that play second base: ', second_base_players)
"""

#notes
"""
so for this i did create a bunch of dead dummie files so dont freak out when you see those. 
now i see what he means by regular ecpressions which i would say is a fancy way of saying weird 
syntax. so we used the library of fnmatch and by useing the '*characters you want to be matched
or found' will say to python that those are the ending characters you are looking for. i imagine
there is a ton of these that all do something different and help out a ton when refactoring code.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title3 = "Build a Pretty Price Method in Python"
section_space3 = f'{section_title3}--------------------------------------------'
print(section_space3)

#oh boy here we go. 

import math

def pretty_price(gross_price, corrected_price):
    low_price = math.floor(gross_price)
    corrected_end = str(corrected_price)[-2:]
    final_price = float(f'{low_price}.{corrected_end}')
    return final_price


print(pretty_price(3.21, 0.95))
print(pretty_price(4.76, 99))
print(pretty_price(2.01, 95))
print(pretty_price(3.76, 0.99))

#and bam i did it! not too hard but i definatly had to think about it for a second which is good. 
#now time for jordans soulution. 

def pretty_price2(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension

print(pretty_price2(3.50, 0.95))

#notes
"""
man i can never git it like jordan does lol. i mean both of our work but he didnt even need to 
math library and i didnt need any string conversions. all i had to do it get the float to an int 
was convert it to an int. and for the extension all i had to do was check if it was an int, and 
if it was to multiply it by 0.01 which would make it a decimal. then just return both of them 
summed. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = "Postman Installation Guide for Linux"
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)

#not sure if this will help at all to be honest since i dont run linux very often.

#okay so i did have to install it but it was beyond easy on windows. 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = "Guide to Using Postman for External and Local API Requests on Linux"
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)

#notes
"""
well this guide was very much just for showing how you would use the postman tool to commmunicate
with outside API's, which i do find it much nicer and easier to have that program do it instead of
making a scrapper and getting the data the hard way. i mean i was able to go through it just fine 
and find my way around the program, for what i needed, quite easy so i dont think i need to take too
many more notes unti we work with it more. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title5 = "Environment Setup for Hello World Flask Application"
section_space5 = f'{section_title5}--------------------------------------------'
print(section_space5)