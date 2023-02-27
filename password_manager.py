
#* The point of this project is to have a program that organizes and stores your passwords - We're going to store all the passwords along with the usernames of the account they
#* are associated with in a textfile but we are not going to store the passwords in plaintext - we're going to encrypt them. Since the passwords are going to be encrypted the user
#* is going to have a password to unencrypt them - meaning they need a MASTER password.

#! This project is not meant to be an actual password manager - It's just a fun small project - since there is no Master password.

import os
import getpass
from cryptography.fernet import Fernet
#? This module lets you encrypt text - you need to install this module in order to get it to work - it is not default.
#? you install via the terminal - pip install cryptography

'''
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)
'''
#! This is no longer used after generating the key file - I left it in to be able to go back and see what i did.


# define the name of the file where the encrypted password will be stored
passwordFile = "EncryptedPassword.txt"
key_file = "key.bin"

if os.path.exists(passwordFile):
    with open(passwordFile, "rb") as f:
        encryptedPassword = f.read()

    with open("key.bin", "rb") as f:
        key = f.read()

else:
    masterPassword = getpass.getpass("Enter a master password: ")
    masterPasswordBytes = masterPassword.encode()

    if os.path.exists("key.bin"):
        with open("key.bin", "rb") as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open("key.bin", "wb") as f:
            f.write(key)

    f = Fernet(key)

    encryptedPassword = f.encrypt(masterPasswordBytes)
    with open(passwordFile, "wb") as f:
        f.write(encryptedPassword)
    print("Master password set successfully!")

passwordCheck = getpass.getpass("Enter the master password to check: ")
passwordCheckBytes = passwordCheck.encode()
f = Fernet(key)
decryptedPasswordBytes = f.decrypt(encryptedPassword)
decryptedPassword = decryptedPasswordBytes.decode()

# check if the password entered by the user matches the decrypted password
if passwordCheck == decryptedPassword:
    print("Passwords match!" "\n")
else:
    print("Passwords do not match.")



print("Welcome. You are now in the RazorSharp Password Manager!")

def loadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = loadKey()
fer = Fernet(key)

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            platform, user, passw = data.split("|")
            print("Platform:", platform, "| User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    platform = input("Platform: ")
    name = input("User Name: ")
    pwd = input("Password: ")

    with open("password.txt", 'a') as f:
        f.write(platform + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

