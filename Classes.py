#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title1 = "Introduction to Classes in Python"
section_space1 = f'{section_title1}--------------------------------------------'
print(section_space1)

class Invoice():

    def greeting(self):
        return 'Hi There'

inv_one = Invoice()
print(inv_one.greeting())

#notes
"""
So this is similar to C# but also very differnt in a few different ways. so to make a class it looks very much like C# where you have to call the data type before the name. so you need 
to type class then the name of the class. now the naming convention for classes has it like normal C# where you capitolize the first letters of the names. and you end it like a funciton. 
now one very interesting thing is if you have a function in a class it has to have a default argument of self if you dont have one to pass in. he didn't go into why but made sure to tell 
us that is was needed to avoid an error. now you need to instatiate a class in python instead of invoking in C#. and all that really is, is just an assignment with () at the end of the class
name. if you want to call a function it is almost exactly like C# where is a . then function name followed by (). 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = "Guide to Python's __init__ Constructor Function"
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)

class NewInvoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes:${self.total}'

google = NewInvoice('Google', 100)
snapchat = NewInvoice('SnapChat', 200)

print(google.formatter())
print(snapchat.formatter())

#notes
"""
So im not going to lie this is a bit confusing. so the __init__ constructor function is a way to work with data for functions in the class. so if you were to pass in variables or arguments to the class it can be used 
in the function. so at the top of the class you would make the init function like ' def __init__(self, other arguments): self.otherarg = otherarg' so you are making arguments and then assigning them to the instance of 
the class since its treated like an object you want to make sure it is referenced in the data for the functions since its a new object each time its instantiated. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title3 = "How to Get and Set Data in a Python Class"
section_space3 = f'{section_title3}--------------------------------------------'
print(section_space3)

#use code above for rest of example

print(google.client)

google.client = 'Microsoft'

print(google.client)

#notes
"""
Okay so this is pretty simple and he made it seem scary at first but its actually the same way i use classes in C#. i have not had to make a getter function to get a value from a class. it is almost
the exact same way that i do it in the first place. he did say this isn't the proper way and using the getter functions can be a smarter option but that will be in a later video. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title4 = "How to Work with Python Properties and Decorators"
section_space4 = f'{section_title4}--------------------------------------------'
print(section_space4)

class NewInvoice2:
    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes:${self._total}'

    @property 
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total


microsoft = NewInvoice2('Microsoft', 150)
print(microsoft.client)
print(microsoft.total)
microsoft.client = 'Yahoo'
print(microsoft.client)

#notes
"""
Okay so i was lost at the start but i got there in the end. so this is the setter and getter functions i was talking about last video. and i can see why you would want to do this stratagie though. 
it makes it som much easier to not fuck up the class. so when you make the class and you are doing the self.argname you put one _ for protected and __ for private and then the argument name. then 
in the class you would put @property for the getter function and @argname.setter for the setter function. then go one line down and make a function called the name of the fucntion that has the argument
of self in it. (note for the setter you need to put the argument name you want as an argument as well.) you then retun the self._argname for the getter and assign the self._argname to the argname for 
the setter. what this all really is for is to help other people know what should and should not be touched. if there is a ton of protected variables called and there are no property tags then i should not
call for them. its a good way to communicate to other developers what they should and shouldn't do to not break the class.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title5 = "Overview of Dunder Methods in Python: __init__"
section_space5 = f'{section_title5}--------------------------------------------'
print(section_space5)