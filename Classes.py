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

class Invoice3:

    def __init__(self, client, total):
        self.client = client
        self.total = total
    
    def __str__(self):
        return f'Invoice from {self.client} for {self.total}'

inv = Invoice3('Google', 500)
print(str(inv))

#notes
"""
Okay so this definatly helped clear some things up on dunder functions. so like before dudnder is a function that comes in python but it a private function. which is where the double underscore
comes from. now unlike C# where you have just private and public assignments python utilizes the __ or _ to show its protection level. so its best not to change the functions that you use. the
two dunder fuctions we used in this video is the __init__ and __str__ functions. lets start with the easy one. the __str__ function from what i can see so far is really a way to wrap data you want
into a string. because if you call the str() function and put the instatiated class as an argument, python will search through it for the __str__ function and run it. from what jordan says its a great
debugging tool and i can see. you can easily have what you are reciving just put it all in a string so you can read it. and now that i think about it we just went over init where it is where you can 
assing arguments as data for the rest of the functions and methods in said class. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title6 = "Overview of Dunder Methods in Python: __repr__"
section_space6 = f'{section_title6}--------------------------------------------'
print(section_space6)

class Invoice4:

    def __init__(self, client, total):
        self.client = client
        self.total = total
    
    def __str__(self):
        return f'Invoice from {self.client} for {self.total}'

    def __repr__(self):
        return f'Invoice <value: client: {self.client}, total: {self.total}>'


inv = Invoice4('Google', 500)
print(str(inv))
print(repr(inv))

#notes
"""
So there isn't too much of huge difference between repr and str but the main onw is really what they are used for. repr is what you would use when you want more of a raw data dump. you would use
str when you want to format it and make it look all pretty but you would use repr when you want a data dump or to see what data is coming in at its raw form. to call it from the instantiaed class
is the same way as str but with the repr() function and just pass in the class and the repr function will search through the class for a __repr__ function. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title7 = "How to Build a Custom Iterator Class in Python"
section_space7 = f'{section_title7}--------------------------------------------'
print(section_space7)

class Lineup:
    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player

astros = [
    'Springer',
    'Bregman',
    'Altuve',
    'Correa',
    'Reddick',
    'Gonzalez',
    'McCann',
    'Davis',
    'Tucker'
]

astros_lineup = Lineup(astros)
proccess = iter(astros_lineup)

print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))
print(next(proccess))

#notes
"""
Okay so this was cool. it was a bit like when i built out the number wizard game and had to make my own update funciton but here we are making our own itterator and its all in a class. and i can really start 
to see where the dunder methods and all of that fit it. and after going through it i can see how to make an itterator that fits what you need. over all a good video. i even had to debug some things my self
since they didn't work right away, it was my fault in the end though. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title7 = "Overview of Iterators vs Generators in Python"
section_space7 = f'{section_title7}--------------------------------------------'
print(section_space7)