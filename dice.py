import random

response = input("Do you want to roll the dice y or n:")

while response == "y":
    no = random.randint(1,6)
    if no == 1 :
        print(" --- ")
        print(" -@- ")
        print(" --- ")

        
        response = input("Do you want to roll the dice y or n:")
    elif no == 2 :
        print(" --- ")
        print(" @-@ ")
        print(" --- ")

        response = input("Do you want to roll the dice y or n:")

    elif no == 3 :
        print(" -@- ")
        print(" @-@ ")
        print(" --- ")


        response = input("Do you want to roll the dice y or n:")

    elif no == 4 :
        print(" -@- ")
        print(" @-@ ")
        print(" -@- ")


        response = input("Do you want to roll the dice y or n:")

    elif no == 5 :
        print(" @-@ ")
        print(" -@- ")
        print(" @-@ ")

        response = input("Do you want to roll the dice y or n:")

    elif no == 6 :
        print(" @-@ ")
        print(" @-@ ")
        print(" @-@ ")

        response = input("Do you want to roll the dice y or n:")

    

    
