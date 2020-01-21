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
formatted_tags = '+'.join(tags_three)
query_tags = f'{uri}{formatted_tags}'

print(query_tags)