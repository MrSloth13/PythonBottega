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

"""
sum_test = 23 + 54 + 223
converting_test = [23/sum_test, 54/sum_test, 223/sum_test]
converting_sum = sum(converting_test)
print(sum_test)
print(converting_test)
print(converting_sum)
"""

import operator
import numpy as np
from numpy.random import choice

weights = {
  'winning' : 0.1,
  'you_live' : 0.3,
  'taking_an_L' : 0.6,
}

weights2 = {
  'winning' : 23,
  'you_live' : 54,
  'taking_an_L' : 223,
}

def totally_fair_lottery(the_odds):
  dictionary_nums = list(the_odds.values())
  dictionary_strings = list(the_odds.keys())
  dictionary_nums_sum = sum(dictionary_nums)
  dictionary_nums = [ round(nums / dictionary_nums_sum, 2) for nums in dictionary_nums]
  print(dictionary_nums)

  return choice(dictionary_strings, p=dictionary_nums)

print(totally_fair_lottery(weights2))
print(totally_fair_lottery(weights2))
print(totally_fair_lottery(weights2))

#okay so i got my version working!!! fucking christ that took days of work and reasearch but i got it in the end. now i have to watch the rest of the video and see how close i was and what other way Jordan did it. 

#Jordans way

def weighted_lottery_function(the_weights):
  container_list = []

  for(name, weight) in the_weights.items(): #this will look for the key and value pairs in the, which you can put in () and looping through the dictionary name with the item function which is what will give the first part their return.
    for _ in range(weight): # this will look at every element in the list at the range of the value the first loop found, then append or add that name to the list. 
      container_list.append(name)

  return np.random.choice(container_list) #the last part is just using the random.choice function which will pick a random item inside of a list. since you populated the list with a ton of elements in relation to there odds, it will be weighted even at random


print(weighted_lottery_function(weights2))
print(weighted_lottery_function(weights2))
print(weighted_lottery_function(weights2))

#notes
"""
Okay so he did a very different approach and did it almost all manually. the only part that wasn't was the random choice part which i also used numpy's choice funciton but in a totally differnt way. i do think his works better for 
smaller dictionaries but i think mine might work better with larger ones since mine doesn't need to loop and make a list that contains all the keys as many times as the value is. i do, for the msot part understand how he did it now after seeing it. 
i definatly made it a bit harder on my self but i got there in the end and i did understand the directions in the first place this time i just struggled with understanding some of the more broad concepts in this project like odd and numpy. 
like i said i got there in the end but it definatly wasn't easy. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title15 = 'Overview of Python Dictionaries'
section_space15 = f'{section_title15}--------------------------------------------'
print(section_space15)

# in this section we will be over the dictionary data type

# a dictionary is a key, value data structure

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

second_base = players['2b']
designated_hitter = players['DH']

print(second_base)
print(designated_hitter)

#notes
"""
Okay so after the last project i better fucking know a good amount about how dictionaries work in python. I did however learn the proper way to call a key  for a value. the syntax is almost exactly like a list, but instead of 
having somthing like an index you would use words or strings to find the value you want. and you would use a key(string) to find the corrisponding value. the name kinda tells you how it works, at least i feel it does, but it 
is most definatly not a list. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title16 = 'Guide to Nested Collections in Python Dictionaries'
section_space16 = f'{section_title16}--------------------------------------------'
print(section_space16)

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angles" : ["Trout", "Pujols",],
  "yankees" : ["Judge", "Stanton"],
}

yankees_team_list = teams['yankees']

print(teams['astros'][0:2])
print(teams['yankees'][1])
print(teams['angles'][:])
print(yankees_team_list)

#notes
"""
so this was cool and i was even able to predict how some of the syntax would work for it. so the keys have to be a string to there really is no changing that but the value can be any data type that you want it to be. in this case 
we made the data type a list. now when you call the list you would just call the dictionary and pass in the key for the value you want. the really nice part is after you close out with the last ] you can treat it like any other list. 
so if you wanted to grab a slice of the list you could just put [:3] after and it will slice the value that is returned. this goes for any functions you want or can call on a list type. and like normal you can also store the value
in an another variable. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title17 = 'How to Add New Key/Value Pairs to Python Dictionaries'
section_space17 = f'{section_title17}--------------------------------------------'
print(section_space17)

teams2 = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angles" : ["Trout", "Pujols",],
  "yankees" : ["Judge", "Stanton"],
}

teams2['red sox'] = ['Price', 'Betts'] # this is the syntax for adding a new key/value pair. pretty straight forward

print(teams2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title18 = 'Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values'
section_space18 = f'{section_title18}--------------------------------------------'
print(section_space18)

teams3 = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angles" : ["Trout", "Pujols"],
  "yankees" : ["Judge", "Stanton"],
}

featured_team = teams3['yankees']
cool_team = teams3.get('mets', 'No featured team') # get takes two arguments. first is the key you want to look up or find, second is what you want to be returned or to be the value of that key if it is not found in said dictionary. 
real_cool_team = teams3.get('yankees', 'No cool team')

print(teams3)
print(cool_team)
print(real_cool_team)

#notes
"""
This is really helpful and will probably use this from now on, its also best practice so should do it anyway. so if you try to query a key that you know all is right with the world. now if you try to query a key that does not exist 
the program will error out. this is good since you dont want to not know that the key doesn't exist but at the same time you dont want an error. so you can use the .get function which takes two arguments. the first is the key you
want to look and find, the second is what you want it to return or the value incase there isn't one already. so it acts very much like a conditional or if/else statement. so it will look for the key you asked for, if it is found it 
will return what is actually attached to the key and ignore the second argument in the get function, but if it is not found it will return what you put the second argument in the get function as. very useful. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title19 = 'Guide to Python Dictionary View Objects'
section_space19 = f'{section_title19}--------------------------------------------'
print(section_space19)

players4 = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(players4.keys())
print(players4.values())
print(players4.items())

print(list(players4.values())[1])

player_names = list(players4.copy().values()) 
"""
this is what you would call 'thread safe'. by making a copy of the dictionary you cut off the dynamically updating thread which could give you a different result if some one is 
making a change to the list. so you would copy first then take your keys, values, or items.
"""

print(player_names)

"""
all three of the functions above are what is called a view object. they provide a dynamic view on the dictionary's entires, which means that when the dictionary changes, the view reflects these changes. so if i am understanding this 
correctly this means that if we have a variable that we assigned one of these two, it will always keep up to date with the original dictionary. one important thing to note is you can not treat these view objects like normal values. 
you would have to convert them like i did for the lottery function to be able to interact with the data type you need them to be.  
"""

teams4 = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angles" : ["Trout", "Pujols"],
  "yankees" : ["Judge", "Stanton"],
  "red sox" : ["Price", "Betts"],
}

team_groupings = teams4.items()

print(list(team_groupings))
print(list(team_groupings)[1])
print(list(team_groupings)[1][1])
print(list(team_groupings)[1][1][0])

#notes
"""
So some of this i was a bit ahead on since i used some of it to make my lottery funciton work. some concepts were new and man there was a ton in this long video. so to start what the .key, .value, and .items return is a dictionary 
view object. which is fancy for saying its a lived updated variable. so if there is a change made it will change the data you are working with. that leads into the concept of 'thread safty' which is the practice of cutting the tread
or the live updating side of it so your data is static at the time of excicution. the primary way to do this is to convery the view object to a list and then call the .copy function which will make a copy of the dictionary first and 
then that is what is used for any furuther .key, or .value function you want to throw at it. now if you want to access collections nested inside of the dictionary you would first need to convert the view object into a list again, then
you can just treat it like a list. you would call an index in []. you would then just follow down the line if you would want to go deeper by just putting another pair of [] right after the last one. so i was very right to convert the 
view objects in my lottery function over to a list to be able to work with them like a list. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title20 = 'Overview of the Multiple Methods for Deleting Items in a Python Dictionary'
section_space20 = f'{section_title20}--------------------------------------------'
print(section_space20)

teams5 = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angles" : ["Trout", "Pujols"],
  "yankees" : ["Judge", "Stanton"],
  "red sox" : ["Price", "Betts"],
}

del teams5['astros'] #this is the first way you can delete an item from a dictionary. you would call del then the name of the dictionary, then pass in the key you would want to delete. this will delete the values as well. 
"""
note that the above example will error out if there is not a key in the dictionary that you want to delete. and no you cant use the get function on it to get around it like we did for looking up a key.
"""

teams5.pop('yankees', 'There is no key here') #this works just like the get function but will delete a key/value pair in a dictionary.
removed_team = teams5.pop('mets', 'there is no key here') #the one trick to pop is it will return a value so if you just call the dictionary it will just return in, you will have to assign it to a value to see it. 

print(teams5)
print(removed_team)

#notes
"""
So here are two ways to delete items from a dictionary. now del is short and sweet but you have to know for a 100% certainty that you know what you want to delete. if not then you can do the slighlty longer version
with pop and that way it doesn't error out. reallistically i will probably be using both depending on weather i know what will be deleted or not. other then that this was a short and nice video. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title21 = 'Guide to Working with Lists of Nested Dictionaries'
section_space21 = f'{section_title21}--------------------------------------------'
print(section_space21)

new_teams_list = [
  {
    "astros" : {
      "2B" : "Altuve",
      "SS" : "Correa",
      "3B" : "Bregman",
    }
  },
  {
    "Angles" : {
      "HF" : "Trout",
      "DH" : "Pujols",
    }
  },
]

print(new_teams_list)

print(new_teams_list[1].get('Angles', 'no team').get('DH', 'no team')) #this is one way to get down to the data you want. simply by going through each one and just doing what i would normally do to grab the data i want.

team_angles = new_teams_list[1].get('Angles', 'no team') #this is another way combined with the print statment below. both would work but my first one can be quite a long horizontal line while jordans would be more vertical

print(list(team_angles.values())[1])

#notes
"""
So i definalty was able to guess a way to get to the same data as jordan demonstrated but i can also see how good his way it. mine is a very blunt force way of doing it while i feel jordans has a better scalability
with his approach. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title22 = 'Build a Histogram in Python with No 3rd Party Libraries'
section_space22 = f'{section_title22}--------------------------------------------'
print(section_space22)

#a histogram is it's a type of chart used in statistics and machine learning that allows you to see patterns and basic types of trends with data.

"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$

g = google
f = facebook
t = twitter
o = offline

$ = sales
"""

sales_figures = {
  'Google' : f'g {20 * "$"}', #this is very cool. so you cant do something like 4 + 'w' but you can do 4 * 'w' and it will just replicate the string for how ever times you multiplied it by.
  'Facebook' :f'f {42 * "$"}',
  'Twitter' :f't {10 * "$"}',
  'Offline' :f'o {12 * "$"}',
}

print(sales_figures['Google'])
print(sales_figures['Facebook'])
print(sales_figures['Twitter'])
print(sales_figures['Offline'])

print(list(sales_figures.values()))


"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

#jordans result

jordan_sales = {
  'google': 20,
  'facebook': 42,
  'twitter': 10,
  'offline': 12,
}

print('g ' + jordan_sales['google'] * '$')
print('f ' + jordan_sales['facebook'] * '$')
print('t ' + jordan_sales['twitter'] * '$')
print('o ' + jordan_sales['offline'] * '$')

#notes
"""
So im not sure if i did it wrong or if i did it really right lol. so i put the string interpolation in the dictionary itself while jordan did it in the print statement. it wasn't clear if it was 
suppose to be in one of the other so i only did it the way i first though of and ran into no errors. so yay me i think. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title23 = 'Introduction to Python Tuples'
section_space23 = f'{section_title23}--------------------------------------------'
print(section_space23)

#now on to the last one. tuples. very similar to list.

# List: []
# Dictionary: {}
# Tuple: ()

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

title, sub_heading, content = post #this is 'unpacking'

print(sub_heading)

# Tuple: immutable
# List: mutable

#notes
"""
So from what i can see, besides the obvious syntax, the main difference is that like a string a tuple is immutable. so this means you cannot change the original tuple. where as a list can be changed. for example if you were to unpack
a list it would work at first. but if the order of the list or an extra item is added, it will change the unpacking which can really mess things up. where as if it was a tuple, it could not be changed so it would have to be reassigned 
which would cause you to unpack a second time which should account for the changes. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title24 = 'How to Add Elements to a Tuple by Leveraging Re-Assignment'
section_space24 = f'{section_title24}--------------------------------------------'
print(section_space24)

post2 = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post2))

post2 = post2 + ('Published',) # it is very important to add a comma at the end so python knows its a tuple, otherwise it will treat it like a string
post2 += ('Deleted',)

print(post2)
print(id(post2))

#notes
"""
So Tuples are quite a bit like string due to there immutablilty. one thing to keep note of is when you are adding an single element or mulitple you need to end the list of items with a comma just before you close out the (). this 
way python know that you are adding a tuple and not trying to add a bunch of strings. one really cool thing he showed is the id function. this will give you the unique identifier number for the location of that data on RAM or harddrive
space. you can see if you reassign a value it will get a new id but the original one is still the same. you are just performing an override for any later use of that variable name. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title25 = 'Working with Lists Nested in Tuples'
section_space25 = f'{section_title25}--------------------------------------------'
print(section_space25)

post3 = ('Python Basics', 'Intro guide to python', 'Some cool python content')

post3 += (['Thomas', 'Betty', 'Jordan'], 'Mountains', 'Tuna',)

print(post3)

the_top, the_middle, the_end, the_class, extras, last = post3

print(the_class[1])
print(last)

#notes
"""
So this is very straight forward. honestly
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title26 = 'Guide to Slices in Python Tuples'
section_space26 = f'{section_title26}--------------------------------------------'
print(section_space26)