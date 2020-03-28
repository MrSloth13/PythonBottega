import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('text files:', file)

        if fnmatch.fnmatch(file, '*.rb'):
            print('ruby files:', file)

# list_files()


players = [
    'Jose Altuve 2B',
    'Carlos Correa SS',
    'Alex Bregman 3B',
    'Scooter Gennet 2B'
]

second_base_players = [player for player in players if fnmatchcase(player, "*2B")]

print(second_base_players)
print('players that play second base: ', second_base_players)