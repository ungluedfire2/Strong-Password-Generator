import pickle
import random
import os
import pip

lower_case = "abcdefghijklmnopqrstuvwxyz"
uper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + uper_case + number + symbols
length_for_pass = 12

print("-- COMMANDS LIST -- \n -generate - generates a password \n -load - loads a saved password \n --- \n -save - to save the password (can only be used after the [generate] command)\n -skip - to not save the password (can only be used after the [generate] command)\n ---")

def start() :
    password_generate = input("")

    if password_generate == "generate":
        password = "".join(random.sample(Use_for, length_for_pass))

        print("Your password is : " + password + "\n ")

        save = input(" ")

        if save == "save":
            name = input("Name : ")
            f = open(name, "w+")
            f.write(password)
            f.close()
            start()
        elif save == "skip":
            start()

    elif password_generate == "load":
        load_name = input("Name : ")
        f = open(load_name, "r")
        print(f.read())
        f.close()
        start()
start()