import hashlib
import os
import time
import random
import sys

passwordList = []
loginSuccess = 0

def start():
    opt = str(input("Would you like to login to an account, register, delete account, change a password or cancel?? Type 'Login' to login, 'Register' to register, 'Change' to change, 'Delete' to delete and 'Cancel' to cancel"))
    opt = opt.lower()
    if opt == "login":
        login()
    elif opt == "register":
        createFile()
    elif opt == "change":
        changePass()
    elif opt == "delete":
        delete()
    elif opt == "cancel":
        sys.exit("Cancelled")
    else:
        print("Not a valid response")

# defines the function for finding a file
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))


# defines the function for reading and printing a file (do not use)
def findFile():
    userFind = str(input("What is your username?  "))
    with open(userFind + ".txt") as f:
        contents = f.read()
        print(contents)


# defines the function for creating a new account
def createFile():
    username = str(input("Enter a username  "))
    passInput = str(input("Enter a password  ")).encode()
    inputHash = hashlib.sha512(passInput).hexdigest()
    myFile = open(username + ".txt", "a")
    myFile.write(inputHash)
    myFile.close()
    print("User created")
    start()

# defines the function for logging in (obviously)
def login():
    userLogin = str(input("Please enter your username:  "))
    passLogin = str(input("Please enter your password:  ")).encode()
    passLoginHash = hashlib.sha512(passLogin).hexdigest()
    with open(userLogin + ".txt") as f:
        contents = f.read()
    if passLoginHash == contents:
        print("Login successful!")

    else:
        print("Incorrect username or password")

    start()

#changing password function
def changePass():
    print("You have chosen to change your password")
    print("Please login first")

    userLoginChange = str(input("Please enter your username:  "))
    passLoginChange = str(input("Please enter your password:  ")).encode()
    passLoginHashChange = hashlib.sha512(passLoginChange).hexdigest()
    with open(userLoginChange + ".txt") as f:
        contents = f.read()
    if passLoginHashChange == contents:
        print("Login successful!")
    else:
        print("Incorrect username or password")
    user = userLoginChange

    passChange = str(input("What would you like your new password to be?   ")).encode()
    passChangeHash = hashlib.sha512(passChange).hexdigest()

    file = open(user + ".txt", "w")
    file.truncate()
    file.write(passChangeHash)
    file.close()

    print("Password change successful")
    start()

#returns an error rather than deleting the account anyway if you get the password wrong, it doesnt delete the file and i cannot be bothered to debug it rn
#i am fixing it now so ignore that last comment
#but there is only 3 mins left of computer science D:
def delete():
    loginSuccess = 0
    sure = str(input("Are you sure you want to permanently delete your account? y/n"))

    sure = sure.lower()

    if sure == "y":
        print("You have chosen to delete your account")
        print("Please login first")

        userLoginDelete = str(input("Please enter your username:  "))
        passLoginDelete = str(input("Please enter your password:  ")).encode()
        passLoginHashDelete = hashlib.sha512(passLoginDelete).hexdigest()
        with open(userLoginDelete + ".txt") as f:
            contents = f.read()
        if passLoginHashDelete == contents:
            print("Login successful!")
            loginSuccess = 1
        else:
            print("Incorrect username or password")

        user = userLoginDelete

        if loginSuccess == 1:
            isfile = os.path.isfile(user + ".txt")

            os.remove(user + ".txt")
            print("Account deleted")

    elif sure == "n":
        print("You have chosen not to delete your account")
        time.sleep(5)

    else:
        print("Not a valid response")

    start()


start()

