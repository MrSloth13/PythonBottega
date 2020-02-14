og_guess_max = 1000
og_guess_min = 1
og_guess = 500

def Game_Start():
    global og_guess_max 
    global og_guess_min 
    global og_guess 
    print('===============================')
    print('Welcome to Number Wizard')
    print('Pick a number in your head, but don\'t say it outloud (I\'m listening)')
    print(f'The highest number you can pick is {og_guess_max}')
    print(f'The lowest number you can pick is {og_guess_min}')
    print('Type "higher" if it is higher, "lower" if it is lower, and "same" if i got it right')
    print('if you want to stop at any time, just type "stop" and the game will end')
    print('Now lets get started!')
    print(f'is your number higher or lower then {og_guess}?')

    og_guess_max += 1

    def Next_guess():
        global og_guess_max
        global og_guess_min
        global og_guess
        og_guess = (og_guess_max + og_guess_min) // 2
        print(f'higher or lower then {og_guess}')

    def UpdateCheckOne(response):
        global og_guess_min
        global og_guess
        response 

        if response == 'higher':
            og_guess_min = og_guess
            Next_guess()
        else:
            return True 

    def UpdateCheckTwo(response):
        global og_guess_max
        global og_guess
        response 

        if response == 'lower':
            og_guess_max = og_guess
            Next_guess()
        else:
            return True

    def UpdateCheckThree(response):
        response 

        if response == 'same':
            print('I never loose to a Stupid human HAHAHAHA')
            PlayAgainPrompt()
            return False
        else:
            return True

    def UpdateCheckFour(response):
        response

        if response == 'stop':
            exit()
            return False
        else:
            return True

    def Restart(response):
        global og_guess_max
        global og_guess_min
        global og_guess
        response

        if response == 'y':
            og_guess_max = 1000
            og_guess_min = 1
            og_guess = 500
            Game_Start()
        else:
            return True

    def Game_end(response):
        response

        if response == 'n':
            exit()
        else:
            return True

    def PlayAgainPrompt():
        print('would you like to try again?')
        print('type "y" for yes, and "n" to exit')

        while True:
            what_you_doing = input()
            Game_end(what_you_doing)
            Restart(what_you_doing)


    def Loop():
        while True:
            what_you_doing = input()
            UpdateCheckOne(what_you_doing)
            UpdateCheckTwo(what_you_doing)
            UpdateCheckThree(what_you_doing)
            UpdateCheckFour(what_you_doing)


    Loop()


Game_Start()

