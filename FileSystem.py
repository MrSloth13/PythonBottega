#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title1 = "How to Create and Write to a File in Python"
section_space1 = f'{section_title1}--------------------------------------------'
print(section_space1)

file_builder = open('logger.txt', 'w+')

for i in range(100):
    file_builder.write(f'Im on line {i + 1}\n')

#file_builder.write('Hey, Im in a file')

file_builder.close()

#notes
"""
This is really fucking cool lol. i finally feel like i am making something or learning what i need 
to actually make something. so to start if you want to open a file you would use assignment and use
the 'open()' function within python itself. now that takes two string arguments which are and name
of the file and what permissions you want to allow. i dont know all the permissions but i do now 
know that 'w+' means im allowed to write to the file. one important note is that the open function 
look through the folder to see if it can find any file with that name, if it does not however it 
will create that file for you. so you would use open to open and create files. now he also went over
the write function which you would just call like .write() and put what you want to write to file. 
jordan did warn though that using this syntax by just opening and writing a file will just completly 
re-write the file. the entire thing. so i would only recommend using this exact syntax when working 
with new file and not an existing one. 
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

section_title2 = "Using Regular Expressions to List File Types in Python"
section_space2 = f'{section_title2}--------------------------------------------'
print(section_space2)