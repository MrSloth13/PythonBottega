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