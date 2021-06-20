import os
from random import randrange
from time import sleep

max = 3
arr = [randrange(0, max), randrange(0, max)]

choice = '_'

score = 0
print(str(arr[-2]) + ' > ' + str(arr[-1]))
sleep(1.5)
while choice != '':

    #os.system('clear')

    arr.append(randrange(0, max))
    #print(arr)
    #print(arr[-1])
    sleep(1.5)
    choice = input("Same " + str(arr[-1]) +" ? Yes or No ?")
    #print(str(arr[-1]) + " " + str(arr[-3]))
    if choice == 'y':
        if arr[-1] == arr[-3]:
            score += 1
            #print("Score: " + str(score))
        else:
            print("Fail")
            break
    elif choice == 'n':
        if arr[-1] != arr[-3]:
            score += 1
            #print("Score: " + str(score))
        else:
            print("Fail")
            break
    else:
        break
print(arr)
print("Bye, your score: " + str(score))