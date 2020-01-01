#String Basics --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

sentence = 'The quick brown fox jumped over the lazy dog'
# sentence = "The quick brown fox jumped over the lazy dog"
# Note that python doesn't care like other languages on which on you use ("" or '') it will treat is as the same. 

print(sentence)

sentence_two = "That is my dog's bowl" # you would want to use one over the other if the content you have uses one of them, use the oppisite on the outside. 
sentence_three = 'That is my dog\'s bowl' # is that is now possible putting a forward slash (honestly i still don't know which is which. it could be a back slash but its the one that is above the enter key on the right of the keyboard) and python will run it correctly
sentence_four = 'Tiffany said, "Thats my dog\'s bowl' #you could even use it mulitiple times through out the sentence and it will still work with the forward slash. 

print(sentence_two)
print(sentence_three)
print(sentence_four)


#Python String Case Funcitons ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# so from what i can tell a case for a case fucntion is the abaility to call a function on an object. in the example below, putting a . then the name of the function and followed by () called a funcition to make all characters uppper case. 

sentence_five = 'The quick brown fox jumped'.upper()

sentence_five.upper()  # This will not change the characters. 

print(sentence_five.upper()) #this will work. 

print(sentence_five)

#notes 1
"""
sentence = 'The quick brown fox jumper'
sentence -> variable
'The quick brown fox jumped' -> string
 = -> assignment

okay so this is very interesting. so the reason calling the variable and just adding the case function is because its not a perminate change. so when you ask it to print the sentence again no changes were perminatly made. 
which is also why putting the case function in the print call out did work, it wasn't a perminate change but it was called for the print. So if i am understanding the rules here, the only time a case function is a perminate
change is when you are assigning the object to the variable (making the variable), where if you call the variable later with the case function it will not make a perminate change. i can see where this can be usefull since if you call the 
case function with the vaiable when it is only needed once, and not change the original one, can be very useful for having dynamically changing data. another way around it is to make a new variable that is just the old one with the case
function on it. then call that variable that needs it. 
"""

sentence_six = 'the quick brown fox jumped'.capitalize()
sentece_seven = 'the quick brown fox jumped'.title()
sentece_eight = 'THE QUICK BROWN FOX JUMPED'.lower()

print(sentence_six)
print(sentece_seven)
print(sentece_eight)

#notes 2
"""
alright so this one is more of just going through other case function that you can use on strings. some things to note are that the capitolize case function will only work on the very first letter. and note that title will capitolize the first 
letter of every word. then obviously lower will make anything in the string lower case. best used when you want to make sure that the text has no capitols in it i suppose. 
"""

# How to Access Portions of Strings in Python----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
well even he said this will be part reveiw and for me it definatly will since i dont quite remember how to in JavaScript but i think i do. hes starting off going over the fact that ranges, or really any kind of counting
is done from a base of 0. so if you hava a list that is 5 items long then the last item in the list is item 4. i know you know what im talking about. when ever you make a string the programming lanuguage will make an index of all the 
items. the first item will be zero and then you can count up from there. remember that spaces count. 
"""

starter_sentence = 'The quick brown fox jumped'
  #index numbers =  0123456789 and so on. 

print(starter_sentence[5].upper())

starter_sentence_two = starter_sentence[5].__add__('hello')

print(starter_sentence_two)

starter_sentence = 'hello'

print(starter_sentence)


#notes 1
"""
So in python strings cannot be changed once they are assigned. i belive you can still reassign the variable but you can not change a part of the string. so you can say starter_sentence = 'something different' and it will still work
but what you couldn't do is say starter_sentence[5] = "y". that will make it error out. so basically when you make a string variable, that strings conent cannot be replaced or changed without reassigning it so something completly different
"""

starter_sentence_three = 'The quick brown fox jumped'

first_word = starter_sentence_three[0:3] #the way ranges work is the cut off is right before the number you put in. so really think about it like counting like normal instead of a base of 0. 

print(first_word)

new_sentence_two = 'Thy' + starter_sentence_three[3:] #leaving it blank will automatically go to the end. 

print(new_sentence_two)

#notes 2
"""
Okay so now i am staring to get it a bit more. the only way we were able to change the original string was to either reassign it entirely or to make a new variable and insert our word and add only the text we wanted after using a range. 
Ranges by the way work really nice but a bit weird in python. so the syntax is inside the [] you would but where you want to start, then a : to separate and say you are calling a range, followed by the number you want it to stop at. note
though that when you give it the last number it will stop before that index number and will only grab everything before it. so when calling out the end of the range you could really just count like normal and put that number in there. if 
you want grab from the very begining or end how ever you would just leave that side of the : blank and python will automatically do the rest.
"""

#Guide To Heredocs in Python---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#so all a heredoc is actually, is a multi-line string in python. i'm not sure if that is what they are called in other languages but in python they are forsure called a heredoc.



content = """
So i need a few different almost pharagraphs of text to try and turn into a multi-line string. 
  and they are also being tabbed in on the second and third line from what i can see. 

And on this one , the one which two lines that are both tabbed, both the second and third line are tabbed in the 
  same amount instead of having the third line be tabbed in by another two spaces which if you
  ask me would be very hard to keep track of. and this is hard to just come up with sentence on the fly

And finally we make it to the last one and it is also the shortest one out of the bunch, while 
  not quite being one line.
""".strip()

print(content)

#notes 1
"""
So this was easy but also very helpfull. if you look in the example above we wanted to make the whole thing, including the spaces, into a single string that could be printed to the console. now if you just try to make this like a normal
string it won't work. as soon as there is a space between lines or a line between lines it will error out since its looking for the end of the string. but if you put ''' in front and behind of the start and end of the whole string it will 
work. now if you use the exact syntax as above then you will need to use the .strip() function to take away any empty lines that wernet originally there. the only other way to fix this is to have the ''' right next to the start and the 
end of the string. if you put it above and below like above example the strip function is the only other way to fix that issue. 
"""

#How to Build a Raw Multiline String in Python--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# content_two = """
# So i need a few different almost pharagraphs of text to try and turn into a multi-line string. 
#   and they are also being tabbed in on the second and third line from what i can see. 

# And on this one , the one which two lines that are both tabbed, both the second and third line are tabbed in the 
#   same amount instead of having the third line be tabbed in by another two spaces which if you
#   ask me would be very hard to keep track of. and this is hard to just come up with sentence on the fly

# And finally we make it to the last one and it is also the shortest one out of the bunch, while 
#   not quite being one line.
# """

# print(repr(content_two))

long_string = '\nSo i need a few different alomost phoragraphs of text to try and turn into a multiline string\nand they are also being tabbed in on the second and third line from what i can see\n\nand on this one, the one which two line that are both tabbed, bothe the second and third liend are tabbed in the same\n'

print(long_string)

#notes 
"""
So for this im still a bit confused on what i did wrong with the long_string the first time since it just kept giving me a syntax error even though i did the same thing as jordan. either way i went in a manually typed it and it seemed to work 
just fine for me. so first we went over the repr() function and what that is, or what its short for is representation, so it will show you what python is seeing and interpreting. when you do that you will see a bunch of \n appear all over
the text and all the line spaces taken out. well that is what the \n's are for. anywhere there is a line break there will be a \n. you can see my example above on how that works. this is important since when you are working with API's they 
will only send over raw data and you need to be able to format that. as far as formating goes, all i can see you do is just put the raw string with all the \n's in it into a single normal string and it will do the conversion and formating for
you. but none the less you need to know what it is and what to do with it once you have it. 
"""

#Build a Dynamic Reducer in Python--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
dynamic_reducer([1,2,3], '+') #6
dynamic_reducer([1,2,3], '-') #-
dynamic_reducer([1,2,3], '*') #6
dynamic_reducer([1,2,3], '//') #-
"""
"""
okay so some of the things jordan is telling me that need to be imported are operator and reduce from functools. 
then i need to make a function called dynamic reducer that can take in a list argument and a +,-,*,/ operator as a string and preform the nessasary
proccesses to reduce the list down to a single number. will have to do some reasearch and will probably take most of the day. 
"""

"""
okay so if i'm thinking of this correct in the function i will need to take the passed through list and perform the second argument of the operator in a for each loop. so in theory is would go through each element and perform the operator that was passed in. 
"""

#reasearch notes
"""
so from what i can find online so far is that a reduce function takes in a function, and a list. it will apply that funcion to all the list elements. 
"""
#all of the things i needed to import for this to work. with the exception of operator if i'm looking at things correctly. 
import functools
import random
import operator
from functools import reduce

#some of the inital code to get the reduce function to work with randomly generated operators to make sure that i was getting a different result to show it working just by running the program again. 
"""
ran_number = random.randint(0,3)

print(ran_number)

lis = [ 1 ,2 ,3 ,4 ,5 ,6 ,9 , ]
lis_three =['a+b', 'a-b', 'a*b', 'a//b']

print(functools.reduce(lambda a,b: eval(lis_two[ran_number]),lis))
"""

"""
some of the answers i get:
-28
6480
0.00015432098765432098
30

So it works!!! holy shit. now i need to get it in a funciton that can take the random number generator or a manual one. 
"""

def random_dynamic_reducer():
  ran_number = random.randint(0,3)
  lis = [ 1 ,2 ,3 ,4 ,5 ,6 ,9]
  lis_two =['a+b', 'a-b', 'a*b', 'a/b']

  print(functools.reduce(lambda a,b: eval(lis_two[ran_number]),lis))

random_dynamic_reducer()

"""
alright so there is the function that will work with random generation but no pass in. that is seeming harder then fist expected. 
"""



def dynamic_reducer(passed_list, passed_operator):
  print(functools.reduce(lambda a,b: eval("a" + passed_operator + "b"),passed_list))

dynamic_reducer([ 1 ,2 ,3 ,4 ,5 ,6 ,9], "*")

# victory notes!
"""
Oh man that was a challenge forsure but by the end i definatly see why he left us to research that on our own. i need to be able to be givin a problem and figure it out from my own means. which really means searching the internet but for 
something like a programming language its either that or some books and i dont just have a bunch of python 3 books laying around and there are also not always that best examples there for me so the internet works out well for something like 
research on stuff like this. i also really understand making a function that has variables that you pass in and call when you call the function. over all a very good lesson for me today. i did waste a ton of time slacking off since i really 
had no idea on where to start but once i sat back down and just hammered my way through it i got it in the end. now to see what the rest of the video will show and to see how differently jordan did it and or if i really did it right. based off
his instructions i do feel i acchomplished the mission on this one. 
"""

# now back to the video to see if i did it correctly. 

"""
def jordans_dynamic_reducer(collection, op):
  operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
  }

  return reduce((lambda total, element: operators[op](total, element)), collection)


  
print(dynamic_reducer([1,2,3], '+')) 
print(dynamic_reducer([1,2,3], '-')) 
print(dynamic_reducer([1,2,3], '*')) 
print(dynamic_reducer([1,2,3], '/'))
"""

#final notes
"""
Wow so i did get it right but not in any way he showed and mine is even shorter somehow. guess i just got really lucky on this one. its very different the way he went about it. he made a library, which is shown above as an operators, which 
would assign a givin input with a corrisponding function. so when you passed in the correct operator, the function would then perform the correct operator. when it came to reduce we were mostly on the same page with lambda but where we differ
is where i call eval he just puts the library name followed by [] with the passed in string in there, followed by what i have as (a,b) in () for some reason. that is the only part i dont fully understand but i'm sure i will figure it out one day. 
"""

# Guide to Modern Python String Interpolation---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
