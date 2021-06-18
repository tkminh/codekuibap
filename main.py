import os
from time import sleep

### VARIABLES ###
choice = ''

### FUNCTIONS ###
def display_welcome():
    
    print("\t**********************************************")
    print("\t***    Codekuibap - Hello old friends!     ***")
    print("\t**********************************************")

def display_options():
    print("\nQ1\n")
    print("\nQ2\n")
    print("[q] Quit.")
    return input("What would you like to do? ")

### MAIN PROGRAM ###

while choice != 'q':  
    display_welcome()
    choice = display_options()

    if choice == '1':
        print("\nAnswer 1.\n")
    elif choice == '2':
        print("\nAnswer 2!\n")
    elif choice == 'q':
        print("\nThanks you. Bye.")
    else:
        print("\nI didn't understand that choice.\n")

