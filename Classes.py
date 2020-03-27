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

class Lineupgenerator:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.players[idx]
            else:
                idx = 0
                yield self.players[idx]

            idx += 1

    def __repr__(self):
        return f'<InfinateLineup({self.players})'

    def __str__(self):
        return f'IninateLineup with players: {self.players}'


full_lineup = Lineupgenerator(astros)
astros_newlineup = full_lineup.lineup()

print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))
print(next(astros_newlineup))


print(repr(astros_newlineup))
print(str(astros_newlineup))

#notes
"""
This is interesting. so we did the same thing as we did in the last video but we used a generator instead of an itterator. and one big thing to notes is to generate something you would use the keyword of 
yeild. so its a bit like instatiate in C#. if i had to choose between making one or the other (itterator vs generator) i would actually probably rather use the itterator. and the only reason is you have to 
make and work with an infinate loop which if i dont do it right. i do see jordans point where it is easier to read forsure. i have an easier time processing the itterator in my head then the generator haha. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title7 = "Class vs Instance Attributes in Python"
section_space7 = f'{section_title7}--------------------------------------------'
print(section_space7)

#if i was to guess what this video has to deal with its the fact that an instance of a class is not the same as the class and will probably be stored in a different part of memory. we will see though. 

class Website:
    def __init__(self, title):
        self.title = title


ws = Website('My Website Title')
print(ws.__dict__)

ts = Website('New Title')
print(ts.__dict__)

class Website2:
    title = "My best class title"


dw = Website2()

print(dw.__dict__)
print(dw.title)

#notes
"""
So this is interesting especially after thinking about classes in C#. so a class attribute is not what we have been covering but is what i have done in C#. where you use a class to store either values 
or functions. i have not yet pushed new values to classes an a new instance in C#. but that is what we have done so far in python. which is interesting because the class attributes work almost just like
C# but all of the instance attributes can be interacted with like class attributes but also have another way of doing it. with dunder methods and what not. so in short a class attribute is specific to the 
class itself and will remain constant in each instantiation while an instatntiated attribute will only apply to that one instance and not effect the over all class. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title8 = "Introduction to Inheritance in Python"
section_space8 = f'{section_title8}--------------------------------------------'
print(section_space8)

class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'


class AdminUser(User):
    def active_users(self):
        return'500'

tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')
kristine = User('kristine@devcamp.com', 'Kristine', 'Miller')

print(tiffany.active_users())
print(tiffany.email)
print(kristine.email)
print(tiffany.greeting())


#notes
"""
Well that was definatly different then i thought it was going to work. so if you want a class to inherit from another when you make the class, before you put the : you put (name of class you want to inherit 
from) and bam it is inheriting from the other class. you can now just add what ever specialized functions or variables you need. just remember that when you instatiate the class you still need to provide all
the same information you would as if it were the parent class as well as the child class. otherwise it will be missing data. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title9 = "Using Polymorphism to Build an HTML Generator in Python"
section_space9 = f'{section_title9}--------------------------------------------'
print(section_space9)