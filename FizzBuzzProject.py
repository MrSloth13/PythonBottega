"""
Write a program that prints the numbers from 1 to 100
But for miltiples of three print "Fizz" instead of the 
number and for the multiples of five print "Buzz". For
numbers which are muliples of both three and five print
"FizzBuzz".
"""

def fizz_buzz(max_value):
    max_value += 1

    multiple_of_three_check = lambda a: a % 3
    multiple_of_five_check = lambda a: a % 5

    for num in range(1, max_value):
        if multiple_of_three_check(num) == 0 and multiple_of_five_check(num) == 0:
            print('FizzBuzz')
        elif multiple_of_three_check(num) == 0:
            print('Fizz')
        elif multiple_of_five_check(num) == 0:
            print('Buzz')
        else:
            print(num)



fizz_buzz(100)