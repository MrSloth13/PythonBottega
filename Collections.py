section_title1 = 'Section introduction'
section_space1 = f'{section_title1}--------------------------------------------'
print(section_space1)

#notes
"""
So in the last two sections we covered strings and list but in this one we will be getting a bit more abstract with collections. now a collection isnt really a data type is a "collection"
of different or the same data type. in this section we will be going over three data types with list, libararies, and tuples. i think tuples is the one i know the least about at the current
momnet. now a list fucntions a ton like an array from JavaScript or C#. a list or collection of various variables or classes or what ever you want really. now a dictionary or libarary works
with keys. where something has a key which has a corrilating value to it. that could be a funciton or an operator and just a normal variable. now a tuple, from what he has said so far, is 
strucuted much like the list. he didn't go into detail on how its different but says it more like the list rather then the dictonary. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = 'Overview of Lists in Python'
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

#list are not immutable. which means that they can be changed. nice but also can suck. 

"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']

print(users[1])

users.insert(0, 'Thomas')
print(users[0])

users.append('Ian')
print(users)

print(users[2])
print(users[1] + ' ' + users[3])
print([users[3]])

users[4] = 'Victoria'

print(users)

#notes
"""
AS OF NOW list in python are very much arrays from C# with some helpful tools. list being contained in the [] is very familiar, and calling the list name and then calling the index number (note that the index
number starts from zero like other list so you need to start your count at zero) inside of the [] right after the name. using the insert function is really useful since that would have been a pain in C#. the 
append function is exactly what normaly happens in C# when you add something to a list. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title3 = 'Three Ways to Remove Elements from a Python List'
section_space3 = f'{section_title3}--------------------------------------------'
print(section_space3)

users_2 = ['Jelly', 'Patrick', 'Yellow', 'Jack']

print(users_2)

users_2.remove('Yellow') #you put in the value you want to be removed. 
print(users_2)

users_2.insert(2, 'Yellow')
print(users_2)

popped_user = users_2.pop() # pop doesn't take any arguments since it will return the last item in the list. note that it doesn't remove it or delete it, it will return that variable so you can store it or do what you want. 
print(popped_user)
print(users_2) #okay so pop DID remove it from the list but it was returned into a new vaiable. where remove function will just remove it, pop will give it to you to do something with. 

del users_2[1] # this will just delete it. like delete delete it. must put in the index number to delete. 
print(users_2)

#notes
"""
That was cool. pop was definatly the coolest one. what pop does it take the last list item out and returns it to you. so lets say you have a list you data you need to go through. you would make a loop function 
which would pop the list and return the last item, run some functions on it, then since it was removed from the list when you pop again it will just keep going until there is just no list. all the others are pretty
much explained in there little side notes. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = 'Guide to Nested Lists and Best Practices for Storing Multiple Data Types in a Python List'
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)

users_3 = ['Kristine', 'Tiffany', 'Jordan' , 'Leann']

ids = [1,2,3,4]

mixed_list = [42, 10.2, 'Thomas', users_3]

print(mixed_list)
print(mixed_list[2])

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)

nested_list = [users, users_2, users_3, ids]

print(nested_list)

#notes
"""
Okay what is on line 94 is quite dangourous and is not typically reccomended. the problem with have multiple data types in a list is if you are not carful, and you try to iterate over the list with a sum function and it 
hits a string it will error out. the normal way would be to nest list with certain data types in a larger list. this way you could perform the same iterating functions over all in that list with out the worry of an error. 
there are some occasions where you would want to store multiple different data types but you just have to be carful what you perform on the list. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title5 = 'Overview of Python List Query Processes: len(), Negative Indexes, and index()'
section_space5 = f'{section_title5}--------------------------------------------'
print(section_space5)

tags = ['python', 'development', 'tutorials', 'code']

#We are going over common functions that are used on list in python that are built into the language. 

number_of_tags = len(tags)
print(number_of_tags)
print(tags.__len__()) #this will give you the length of the list. 

print(tags[len(tags)-1]) #okay so i went ahead a bit but this works! and you don't need to know the total length to get the right return. so the fact you can call functions & perform operators means i can minus 1 from a total to match index

last_item =tags[-1]

print(last_item)

index_of_last_item = tags.index(last_item)
print(index_of_last_item)

#notes
"""
Wow so man there are a ton of way of going about this lol. i came up with my own and jordan had like 3 of his own. i don't think i can explain as well as the code and the results can but in short len() will give you a list
length, and index() will give you the index number of the value you input. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title6 = 'How to Sort Lists in Python'
section_space6 = f'{section_title6}--------------------------------------------'
print(section_space6)

tags_two = ['python', 'develpment', 'tutorials', 'code']

print(tags_two)

tags_two.sort()

print(tags_two) # by default the sort function will arrange the list by alphabetical importance or order. 

tags_two.sort(reverse=True)

print(tags_two) #this will sort the list in reverse. this is used for numbers a ton so the most new thing can be on the top instead of the oldest which is what you get when you use sort by itself. 

totals = [234, 1, 3, 2535]

print(totals)

totals.sort() #when dealing with numbers sort defaults to sorting based off value. so least value first and highest last. 

print(totals)

totals.sort(reverse=True) #so when you reverse the highest nunber goes last. 

print(totals)

#notes
"""
So this was fun. i can see the reasons one would have to sort a list and the sort function seems like an easy way to sort a list based off some pretty simple needs like having them in a normal
or reversed order based on values or alphabetical order. other then that i dont know how to sort a list down to calling which element i want where. maybe soon but for now the sort function was
a great start. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title7 = 'Using the join Function in Python to Build a URL Query String'
section_space7 = f'{section_title7}--------------------------------------------'
print(section_space7)

uri = 'https://www.google.com/search?q='
tags_three = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags_three) # This is what will join all of the tag list with a '+' inbetween them. you can use any character you want but it is best practice to use a plus for readabilty. 
query_tags = f'{uri}{formatted_tags}' # going back to string interpolation and using the f{} so insert and add two different string variables together. 

print(query_tags)

#notes
"""
So this section was mainly to show how to use the join function. he did it by building a very real world example. the example we made is more or lees the same process that google actually uses
on their system. now they have a much more complicated tagging system but the concept of joining all of the tags together and then combining the tags with with url or uri can give you a search
result that a browser can understand.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title8 = 'Overview of Ranges in Python Lists'
section_space8 = f'{section_title8}--------------------------------------------'
print(section_space8)

tags_four = ['python', 'develpment', 'tutorial', 'code']

tag_range = tags_four[1:2]

print(tag_range) #note that just like in the string section when you put in the second range limit it will stop at that number and only return what was before it. you would need to go one more to 
#include it. 

tag_range_two = tags_four[1:]

print(tag_range_two)#note this will return from the index of one till the end of the list. 

tags_range_three = tags_four[:3]

print(tags_range_three)#note this will give you a return of the start of the list until the element before 3 since it was the limit and will return all before that variable. 

tag_range_four = tags_four[:-1]

print(tag_range_four) #note that this will return everything from the start to everthing until one fromt he end. like string when you use a negitive number it will start from the back of the list

tag_range_five = tags_four[:]

print(tag_range_five) #note that this will return the whole list. not very useful except learning. 

#notes
"""
So from what jordan says this syntax will be very important and used in just about every machine learning program in python. so this is very important that i understand how ranges work in python.
Thankfully they work almost identical to string ranges in python. you would just call [] like you want an index number and then put your range split by a colon. leaving either side blank will have
python go to the very end of either side. using a negitive number will start from the back of the list. the only other notable thing is that the second number you give for the end of the range will
end at that element. which means it wont get returned. only everthing before the limit will be returned. if you wanted that element you would need to go one index number higher to get it returned 
as well. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title9 = 'Advanced Techniques for Implementing Ranges and Slices in Python Lists'
section_space9 = f'{section_title9}--------------------------------------------'
print(section_space9) 

new_tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

new_tag_range = new_tags[:-1:2] #this is interesting. so by adding another colon you introducted a intraval. so lets say you only wanted everyother element in the list you would use 2. if every third you would use 3 and so on. 

print(new_tag_range)

new_tag_range2 = new_tags[::-1] #wow so this is how you would flip an entire list of elements. i think i get it though. by having nothing in the front or the back of the first colon you are taking the whole list into count, then
# you add another colon but when you add a negitive one after a second colon it will reverse it? the very end is still what looses me but i think i can just at least remember the syntax for it for later. 

print(new_tag_range2)

#now he is saying to try and use a sort function to get the same result so we can see why it wont work but i can already see how. since this is a list of strings it would sort alphanumerically and would not use the index number
#but instead the value of the element. you could make a new variable that would get the index number and yada yada but then your talking more code then the simple snytax above. 

sorted_tags = new_tags.sort(reverse=True) # note that this will return 'none' since the sort function doesn't return anything. so you cant assign it. if you just put new_tags.sort(reverse=True) and printed that it would have worked. 

print(sorted_tags)

#notes
"""
So this was definatly a bit more advanced look in list in python. so we went over the slice functionality of python which is really just a range syntax with a second colon and useing a  intraval or a reverse -1 so take slices out of the
list. was shown that the sort function doesn't actually return anything and will just change the list. if you try to assign the newly sorted list into a new variable it will return 'none' and that will be it. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title10 = 'Guide to the sorted Function in Python'
section_space10 = f'{section_title10}--------------------------------------------'
print(section_space10) 

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

sorted_list = sorted(sale_prices) # when using the sorted function you can store the sorted list in another variable. it also doesn't change the original list since you are reassigning the orignial list values to a new variable. 

print(sorted_list)
print(sale_prices)

reversed_list = sorted(sale_prices, reverse=True) # this will reverse the list simply by passing in a second argument. 

print(reversed_list)
print(sale_prices)

#notes
"""
so this was short but effective. i understand the none return before since it was more of a waring saying you are changing the original list but when you use sorted you can store it in another variable which does not effect
the original list. very helpful and will probably try to use this one when i can to try and make sure i don't change the list unless that is what i need to do, in which case i can just use the .sort() function like normal. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title11 = 'How to Find the Median of a Python List with an Odd Number of Numbers'
section_space11 = f'{section_title11}--------------------------------------------'
print(section_space11) 

#a median is the middle value in a list of items. 

"""
Tools:
-math library
-sorted function
-list slicing
-computations
"""

sale_prices2 = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

import math

#my result

sorted_list2 = sorted(sale_prices2) #sorting the list
list_length = len(sorted_list2) # getting the lenght for the list. note that this will only work on an odd number of list items and will return nothing if you have an even number in there since it divides by 2
median_number = sorted_list2[math.floor(list_length/2):-math.floor(list_length/2):math.floor(list_length/2)]

print(sorted_list2)
print(list_length)
print(median_number)

#Jordans result

sorted_list = sorted(sale_prices2)
number_of_sale = len(sorted_list)
half_slice = math.floor(number_of_sale/2)
first_sale_items = sorted_list[:half_slice]
last_sale_items = sorted_list[-half_slice]
median = sorted_list[half_slice: (half_slice + 1)] # now the way jordan did it will allow this to not error out on an even numbered list. im not sure if it finds the true median but it will return an element thanks to the plus 1. 

print(sorted_list)
print(number_of_sale)
print(first_sale_items)
print(last_sale_items)
print(median)

#notes
"""
so this was challenging but i do understand slicing a bit better and when to call the math library. getting the medain was good practice and pretty straight forward. i don't think i can explain too much i think the code speaks for itself. if my example
doesn't seems staight forward enough i also put jordans result which wallks through it in much more detail then i did since i just wanted to get it to work. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title12 = 'Working with the slice Class in Python to Store Slices'
section_space12 = f'{section_title12}--------------------------------------------'
print(section_space12)

tags_seven = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

slice_object = slice(2)
slice_object2 = slice( 0 , 3 , 1)


print(slice_object)
print(tags[slice_object])
print(tags[slice_object2])
print(slice_object2.start)
print(slice_object2.stop)
print(slice_object2.step)

#notes
"""
so this is a very helpful lesson since one of the main reasons you would the slice function that looks like the a range is if you want to store that slice and be able to call it and use it at a later time or on a different data
structure. there are also some helper functions that can tell you the slice start, stop, and step. speaking of which the slice function take in three arguments and they all have to be put in. so if you want to start from the begining of the list
you would have to put a 0. and step has to atleast have a value of 1. by giving it that value it will just return each item in the slice range. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title13 = 'How to Add to a List in Python with Both In Place and Copy Processes'
section_space13 = f'{section_title13}--------------------------------------------'
print(section_space13)

# we are going to see how we can add and change the list. 

new_tags2 = ['python', 'development', 'tutorials', 'code']

#nope
"""
new_tags2[-1] = 'programming' 
print(new_tags2)

This will only replace the last element will the new string

"""

new_tags2.extend(['programming']) #this will add a new element at the end of the list, but like the sort function doesn't reutrn anything so you cant use it to store in a new variable. 
print(new_tags2)

brand_new_tags = new_tags2 + ['HTML'] #this is the way you would add a new element to a list while creating a new list. make sure you have it in [] because you can combine a string with a list. 
print(brand_new_tags)

#notes
"""
pretty simple and straight forward. as you can see from the code above that some of it is familiar and some is new but it all make sense
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title14 = 'Build a Weighted Lottery Function in Python'
section_space14 = f'{section_title14}--------------------------------------------'
print(section_space14)

import numpy as np
from numpy.random import choice

"""
weights = {
  'winning' : 1,
  'break_even' : 2,
  'lossing' : 3
}

weighted_lottery(weights)
"""

#so what i need to build is a function that will take a dictonary and based off the odds in the dictionary return the correct values based off there odds. fun

# def totally_fair_lottery(the_odds):

weights = {
  'winning' : 0.1,
  'you_live' : 0.3,
  'taking_an_L' : 0.6,
}

weights2 = {
  'winning' : 1,
  'you_live' : 5,
  'taking_an_L' : 15,
}

"""
print(weights)

sum_of_weights = sum(weights.values())
print(sum_of_weights)

# def test(value_man):
#   print(value_man)

sure = weights.get('winning')

print(sorted(weights.values())) #will give the numbers sorted from the dictionary
print(sorted(weights)) #will give me the sorted strings alpha-numerically

new_man = weights.values()
new_new_man = weights.keys()

print(new_man)
print(len(new_man))
print(new_new_man)
print(len(new_new_man))

ary_strings = list(weights.keys())
ary_ints = list(weights.values())
print(ary_strings)
print(ary_ints)
print(choice(ary_strings, p=ary_ints))
"""

"""
okay so here is some progress. i can get access to either just the numerical vaules and the string values. next step will be to build that into the function in the begining. 
"""

# test_array = np.array(weights.keys())
# print(test_array)
import operator

def totally_fair_lottery(the_odds):
  dictionary_nums = np.array(the_odds)
  dictionary_strings = list(the_odds.keys())
  dictionary_nums_sum = sum(dictionary_nums)

  return choice(dictionary_strings, p=dictionary_nums)

print(totally_fair_lottery(weights))

weights /= sum(weights) 
print(weights)

"""
sum_test = 23 + 54 + 223
converting_test = [23/sum_test, 54/sum_test, 223/sum_test]
converting_sum = sum(converting_test)
print(sum_test)
print(converting_test)
print(converting_sum)
"""