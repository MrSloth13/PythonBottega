# list of python data types. there are some new ones in here. 
# Booleans- know it. true of false
# Numbers- there will be an enitre section on this since its so complicated. can be anything from standard ints all the way to floats and large numbers. they can even be attached to a number library
# Strings- any type of byte sequence. or really any type or text stored in '' or ""
# Bytes and byte arrays- very high level, only used for advanced python projects
# None- like the null in C#. best for when you want to assign a value to something but you don't know what should be there. since leaving it blank is not a substitute for None. 

# The next four fit into a catagory of data strucutre. its a way to store a collection of data. i'm sure they all do it in a very specific way but all can fit into that family. 
# Lists
# Tuples
# Sets
# Dictionaries
# There will be an entire section on these later so there is no explimation on this one. 

# a Tip Calculator

# meal_completed = True  #Boolean
# sub_total = 100  #Number
# tip = sub_total * 0.2  #Number
# total = sub_total + tip  
# receipt = "Your Total is " + str(total)  #-notice that since it originally tried to use a number it wouldn't work but once you made it a string it mattered wayyyy more. and that is a nice little function that will allow you to take the data from that variable and convert it to a string so you can use it. 
# tip_announcement = "The tip amount was "  + str(tip) + "% of the subtotal $" + str(sub_total)
# print(receipt)
# print(tip_announcement)

# changing the values Refactoring

meal_completed = True 
total = 100 
tip = total * 0.2 
total = total + tip  
receipt = "Your Total is " + str(total)  
tip_announcement = "The tip amount was "  + str(tip) + "% of the subtotal $" + str(total)
print(receipt)
print(tip_announcement)

first = 'Springer'
second = 'Bregman'
third = 'Altuve'

print(second)

second = 'Correa'

print(second)

# Note all this really does is show how to override the original value set to the variable. at the top we refactored some of the variables(just one really) which is
# just a fancy way of saying we simplified the amount of variables we had realizing we could just update one of the variables instead of having two separate ones. 
# One last thing to note is that if you are changing a variable, make sure you are changing it to the same variable as the orginal one had. changing it can lead to a 
# whole web of problems since some functions are checking for variable types and will error out if the type is changed. 


# python comments section


# single line comments

# I'm a single line comments



# inline comments

name = 'Kristine Hudgens' # TODO: Split into tow variables



# multi-line comments

"""
Multi-Line:
okay i just need to make filler text.
okay i just need to make filler text.
okay i just need to make filler text.
"""

# i don't know how i feel about the multi-line comments. since in visual stuio is doesn't highlight it the same as a normal comment. i could make it comfusing but i can probably get use to it. 


