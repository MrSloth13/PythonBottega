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