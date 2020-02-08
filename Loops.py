section_title1 = "Introduction to Python Loops"
section_space1 = f'{section_title1}--------------------------------------------'
print(section_space1)

#i am now out of the data stuctures!!! now onto loops

#notes
"""
So there are two types of list in python. there is a 'for in' loop and a 'while' loop. a for in loop will run through as many items as you have. simple and will be use about 90% of the time. the 
while loop is similar to C# in where if you dont give it an exit point or a point to end it will just go on and crash the system with an infinite loop. but just like it C# the while loop can still 
be useful. especially if you dont want to go through an enitre list to save on resources. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = "How to Implement Python Loops for Lists, Tuples, and Dictionaries"
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)

#so the first 'player' is just a variable you are assigning to be what ever the iterable variable. so what element you are going over. so in a list, the each element of the list will be considered to be the iterable variable.

"""
for a tuple its the exact same syntax. it doesn't matter at all
"""

players_two = {
    '2b' : 'Altuve',
    '3b' : 'Bregman',
    'ss' : 'Correa',
    'dh' : 'Gattis'
}

for position, player in players_two.items():
    print('Postition', position)
    print('Player Name', player)

#notes
"""
So this video was not as long as i thought, probably thanks to the fact the the syntax for list and tuples and the 'for in' loop are the exact same. i think the text and loops above explain it pretty well but 
in short you would call 'for' and the next word you type can be anything you want. it is what will be called the iterable variable. it is the variable that will be filled with each element when it gets looped over. 
so if you have a list of strings, that word after 'for' will become that variable when all elements before it have been looped over. after that word you follow up with 'in' and the next word should be the name of the 
list of the tuple. then a : like a function and bam there you go. a dictionary is a bit different. you would just make two iterable variables, one for the key and one for the value, then when you call in, make sure 
you call the .items() function at the end of the dicionary name. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title3 = "How to Loop Through the Characters of a Python String"
section_space3 = f'{section_title3}--------------------------------------------'
print(section_space3)

alphabet = 'abcdef'

for letter in alphabet:
    print(letter)

#notes
"""
okay so this was a short video and i was able to work ahead to the end before he was half way done lol. i think i am understaning the for in loops much better now. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = "Guide to Looping Over Ranges in Python"
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)

for num in range(1, 10):
    print(num)


for the_num in range(1, 11, 2):
    print(the_num)

#notes
"""
This is interesting. and in playing around trying to get a conditional to work i realize i must be missing something with conditionals because i was not able to get it working. for ranges though i get them a bit more
but they are still just a bit fuzzy. the best way i can desribe them is like a range when you are slicing a list. it is probably important to note that the range function only takes in ints from what i can see. so this
only makes it more inline with the slice from list. the biggest thing they have in common though is that the end of the range will return the value up till that point which is a long way of saying that if you put the max
end of the range to 10 it will stop at 9. since the range will end right before 10 since that is the max. you would have to go one more number greater to get 10 iterations. and for a for in loop range that is all you are 
really doing with range. you are saying how many time the loop will run for. you can add a third argument which is also like slice where it will basically be saying, if you put a 2 as the third variable it will skip every 
other iteration. if you put 3 it will skip 2 before excicuting on an iteration. i think i have a better grasp then i thought i did after explaining it but i should still look into it. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title5 = "Guide to Continue and Break in Python Loops"
section_space5 = f'{section_title5}--------------------------------------------'
print(section_space5)