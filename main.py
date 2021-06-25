import os
from time import sleep

### MY LIBRARIES ###
import util.cmd
import install
#import workout.learn1
#import workout.learn6
#import DSML.learnnumpy
#import DSML.learnpandas
#import DSML.learnmatplot
import DSML.learnscikit
import DSML.learndeeplearning

### VARIABLES ###
choice = ''


### FUNCTIONS ###
def display_welcome():
    print("\t**********************************************")
    print("\t***               Codekuibap               ***")
    print("\t**********************************************")


def display_options():
    print("\n1. Install necessary library\n")
    print("\n2. Doing task\n")
    print("[q] Quit.")
    return input("What would you like to do? ")


def install_test():
    util.cmd.run_command(install.install_beautifulsoup4)
    # util.cmd.run_command(install.install_request)


### MAIN PROGRAM ###
#
# while choice != 'q':
#     display_welcome()
#     choice = display_options()
#
#     if choice == '1':
#         install_test()
#         print("\nAnswer 1.\n")
#     elif choice == '2':
#         print("\nAnswer 2!\n")
#     elif choice == 'q':
#         print("\nThanks you. Bye.")
#     else:
#         print("\nI didn't understand that choice.\n")
