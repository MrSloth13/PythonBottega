#Overview of Number Types in Python--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title1 = 'Overview of Number Types in Pythons'
section_spacer = f'{section_title1}--------------------------------------------'
print(section_spacer)

product_id = 123 # this is an int or an interger. i am familiar with these from C# and it is a whole number basically. really simple. no fraction or anything like that. 
sale_price = 14.99
"""
okay so floats are a bit complicated and i have a better understanding of them now then when i first learned them. so a float is a floating point variable. now there will be a course that will go more in depth 
in on it but it should not just be called a decimal and always used in place of one. in python there is a decimal type which is much more precise then a float. from what i can tell that is the main difference 
between the two. a float will be good for any non-whole or fractional number that doesn't need to be hyper precise. 
"""
tip_precentage = 1/5
new_product = 150

tip_amount = new_product * tip_precentage

print(new_product + sale_price)
print(tip_amount)

#notes
"""
well that was nice to get a catch up on some things i was definatly rusty on. So to start remember back in the string section when we went over how you cant add a string with a number in it with an actual
number data type. well since we are dealing with sub classes now they can be combined in almost any way. so for example and int can be mulitplied by a fraction or a float or the other way around. another 
good refreshing point was that python will automatically determie the data type when the program is ran. there is no need like in C# to call in or float on the variable when you assign in. 
"""

#Mathematical Operators in Python----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = 'Mathematical Operators in Python'
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

