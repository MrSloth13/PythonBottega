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

usersnames = [
    'jon',
    'tyrion',
    'theon',
    'cersei',
    'sansa',
]

#Continue / Break (the two flow operators for this guide)

for username in usersnames:
    if username == 'cersei':
        print(f'Sorry, {username}, you are not allowed')
        continue
    else:
        print(f'{username} is allowed')

for username in usersnames:
    if username == 'theon':
        print(f'{username} was found at index {usersnames.index(username)}')
        break
    print(username)

#notes
"""
This was a very helpful video. especially since i was just talking about not understanding how conditional works in loops and this video helped so much. explaining it is a bit hard but in short you need to give continue or a 
break statment in order to tell the loop what to do when it hits the conditional. if you put continue you need to provide an else statment, if you say break the next line or lines will be what runs otherwise or just an else
statment with out saying else. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title6 = "Overview of While Loops in Python"
section_space6 = f'{section_title6}--------------------------------------------'
print(section_space6)

#now to learn about the while loop.

"""
The key difference between the two is a for in loop you have a clearly defined start and end. now a while loop will not stop at the end of the list. it has to be told when it is to stop. the stoping point is called the 
sentinal value. 
"""

nums = list(range(1,100))

# while len(nums) > 0:
#     print(nums.pop())

# You can see from the example above that you gave a conditional and when that conditional becomes false the loop will stop. 

def guess_who():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '42':
            print('You correctly guessed it!')
            return False
        else:
            print(f'No, {guess} is not the answer, please try again\n')

# guess_who()

#notes
"""
This was one of my favorites so far. i can fully see why you would use a while loop and i even learned how to get input from the console so now i can make that guessing number game from C# into python. now for
while loops i seen a neat thing which is where you just call while True: and the loop will run until something turns it to false. now normally you would just do it with a conditional and when the conditional is 
met you return False. and as the side note on console interaction you can just put input() and the console will wait for a response. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title7 = "How to Combine and Flatten Lists in Python with the For / In Loop"
section_space7 = f'{section_title7}--------------------------------------------'
print(section_space7)

#We are going to see how we can use the for in loop to merge multiple list.

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)

#notes
"""
So this is pretty simple but still very powerful. and it is very good at reinforcing what a for in loop is good for. i  don't think there is much to say here though since i think the code is pretty self explanitory.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title8 = "Introduction to Using List Comprehension in Python"
section_space8 = f'{section_title8}--------------------------------------------'
print(section_space8)

#!!!This will be hard!!!

#list comrehension is we can set up a number of for in loops to function on a single line and generate list from those lines of code. 

nums_list = range(1,11)
# cubed_nums = []

""" This is how it would look if you did it the long way

for num in nums_list:
    cubed_nums.append(num ** 3)

print(cubed_nums)
print(list(nums_list))
"""

cubed_nums = [num ** 3 for num in nums_list] #the way its layed out is the action you want to perfor or what would be in the code block would be first as the action. then you would put from what i can see to be
#normal for in loop syntax. i'm sure this gets way crazier then this but still really cool. do note though that having it all in the [] is what tells python to be generating a list while this loop is going. 

print(cubed_nums)

even_list = [num for num in nums_list if num % 2 == 0] #the first element is the one that gets returned. then you would do the normal for in syntax. then you call the conditional. 
print(even_list)

#notes
"""
Wow so not only was this not as hard as i though, its something i used to get the lottery funciton working. so the way these work is you want to generate a list. so you would make a new list variable and make an empty []. 
inside of that you would start with what you want to get returned, or the action you could say. think of it as the the last bit in the code block of a for in loop that is doing exactyly what you want to do here. after that
you would put what you would normally do to start a for in loop. like for num in nums_list. and bam it will generate a list off of that. now if you want to add a conditional into the mix you would just put the normal 
conditional syntax like "if nums = 4" and put it at the end. really that simple. i guess i can see how for some that might be a challenging concept but i think it is actually pretty straight forward. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#The next section is conditionals so this is the end of the line for loops as of right now. it was a very interesting ride i will say. 