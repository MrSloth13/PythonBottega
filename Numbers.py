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

#Mathematical Operators in Python---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = 'Mathematical Operators in Python'
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

print("Addition")
print(100 + 42)
print("The operator for addition is '+'") #pretty simple. got it

print("---")

print("Subtraction")
print(100 - 42)
print("The operator for subtraction is '-'") #pretty simple. got it

print("---")

print("Division")
print(100 / 42)
print("The operator for division is '/'") #pretty simple. got it

print("---")

print("Floor_Division")
print(100 // 42)
print("The operator for floor division is '//'") # this is cool. so what it does is round DOWN to the lowest whole number. so if its any less then a whole number it will round down. really cool. the result should explain.

print("---")

print("Multiplication")
print(100 * 42)
print("The operator for mulitiplication is '*'") #pretty simple. got it

print("---")

print("Modulus")
print(100 % 42)
print(2 % 2)
print(5 % 2)
print(25 % 2)
print("The operator for modulus is '%'")

"""
okay so this is weird as fuck man lol. so what this does is it will take the number on the left hand side of the % sign and divide it into the number on the left as many time as possible and will return the REMAINDER. so
if i am understanding this correctly it will just tell you what is left over. jordan days he mostly uses it to see if an number is an even or an odd. if you use 2 then it should evenly divide into any size number where as
an odd number should always have atleast 1 left over after dividing by 2. 
"""

print("---")

print("Exponents")
print(100 ** 2)
print(25 ** 2)
print("The operator for an exponent is '**'") #pretty simple. just like normal exponents once you get past the syntax which isn't that weird when you think about it since an exponent is just multiplication. 

#notes
"""
uhmm i think i have covered most of anything in the notes already. modulus was a bit confusing at first but after seeing how it works i understand it and know how i can use it in other types of programs. other then that
it was pretty much what you though most of the time on which character would be for each operator. floor divsion was kinda weird but after seeing the result i understood right away. 
"""

#Guide to the Order of Operations in Python----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title3 = 'Guide to the Order of Operations in Python'
section_space3 = f'{section_title3}--------------------------------------------'
print(section_space3)

calculation = 8 + 2 * 5 - (9+2) ** 2

print(calculation)

#notes
"""
So this really is just pemdas. just like in JavaScript the order of operations is just pemdas. i was able to get the same answer on my own as the program did and i went down the word pemdas and went and did each one in 
the order and got the same answer so i am assuming i am right. short lesson on this one. 
"""

#How to Use Assignment Operators in Python-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = 'How to Use Assignment Operators in Python'
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)

total = 100

print(total)

#notes 1
"""
Okay so i think i totally get this one. i passed out last night before i was able to take notes but i think this is just going over perfoming an operator and assigning a variable at the same time. i had to do this 
for the game to take away one health. all it really is syntax wise is what ever operator you want to perform followed by an equals sign. i'm sure i will have some examples below but it looks the same as C# from what 
i can see so i'm pretty sure that i got this one. 
"""

total += 10
print(total)

total -= 20
print(total)

total *= 3
print(total)

total /= 4
print(total)

total //= 3
print(total)

total **= 2
print(total)

total %= 2
print(total)

#notes 2
"""
Okay so i was completly right lol. it really is the same syntax to C# and works the same too. so when you assign a variable you can perform an operator on it as you are assigning it. i mean i really do already 
know this one since i have used it a ton for games. 
"""

#Decimal vs Float in Python---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title5 = 'Decimal vs Float in Python'
section_space5 = f'{section_title5}--------------------------------------------'
print(section_space5)

product_cost = 88.40
commision_rate = 0.08
qty = 450

product_cost += (commision_rate * product_cost)
print(product_cost * qty) #42962.4

from decimal import Decimal

d_product_cost = Decimal(88.40)
d_commission_rate = Decimal(0.08)
d_qty = 450

d_product_cost += (d_commission_rate * d_product_cost)
print(d_product_cost * d_qty) #42962.40000000000282883716451

#notes
"""
Holy shit lol. i definatly see why one is called more accurate. so if it wasn't clear after that i don't know what is. you can see the answer that the floats gave me vs the decimal and one is way bigger then they other.
its crazy that if it didn't make it a deciaml i would have never known that the answer was that off. some interesting things about using decimals though is for one its the only data type so far in python that i have 
seen that you need to call its type in a way before assigning it. well i guess lets start at the fact that you will need to import the decimal library and the decimal funcitons in like i did above to gain access to
decimals in the first place. otherwise it would always be a float. now the reason you have to call the data type is because you are calling a function and just putting the float in the () of the function. if its any 
suprise the function to make a float a decimal is and i quote "Decimal()". that is it. once you put your float in there it will be treated adn return a decimal when used in a math problem. and from what you can see
above that there is definatly some more precision that was not seen if it weren't for the decimal. 
"""

#How to Convert Between the Integer, Float, Decimal and Complex Numeric Data Types in Python----------------------------------------------------------------------------------------------------------------------------------

section_title6 = 'How to Convert Between the Integer, Float, Decimal and Complex Numeric Data Types in Python'
section_space6 = f'{section_title6}--------------------------------------------'
print(section_space6)

product_cost_2 = 88.40
commision_rate_2 = 0.08
qty_2 = 450

print(int(product_cost_2))

print(float(qty_2))

print(Decimal(qty_2))
print(Decimal(commision_rate_2))
print(complex(commision_rate_2))