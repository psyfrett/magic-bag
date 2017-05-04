#!/usr/bin/env python
'''
look at me go! comments and all
I should comment this when I understand its voodoo
This triple double (or single) quotes removes the missing docstring module warning from pylint
'''
def welcome_message():
    ''' Friendly message to user '''
    best_name_eva = "Async Comp Welcomes you" + "!" * 3
    print("%s" % best_name_eva)

def input_food():
    ''' This is a function and requires a comment to make pylint happy'''
    user_input = input("What is your favorite food?")
    print("you like {}".format(user_input))
    print()

welcome_message()
print() #blank line for spacing
input_food()
