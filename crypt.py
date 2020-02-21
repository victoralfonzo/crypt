import getpass
import os
import time

#set up desktop path
desktop = os.path.join(os.path.join(os.path.expanduser("~"))) + "/Desktop"
intro = """
    
    #    /$$$$$$                                  /$$       #
    #   /$$__  $$                                | $$       #
    #  | $$  \__/  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$     #
    #  | $$       /$$__  $$| $$  | $$ /$$__  $$|_  $$_/     #
    #  | $$      | $$  \__/| $$  | $$| $$  \ $$  | $$       #
    #  | $$    $$| $$      | $$  | $$| $$  | $$  | $$ /$$   #
    #  |  $$$$$$/| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/   #
    #   \______/ |__/       \____  $$| $$____/    \___/     #
    #                       /$$  | $$| $$                   #
    #                      |  $$$$$$/| $$                   #
    #                       \______/ |__/                   #
    
    Reading and writing will be done using user's desktop directory:
    
    """
#generate alphabet array from ascii characters 32 to 126
alph = []
for i in range(32,127,1):
    alph.append(chr(i))

#print all .txt files w/in desktop directory
def printDirectory():
    time.sleep(0.2)
    print(desktop)
    dirs = os.listdir(desktop)
    exists = False
    for file in dirs:
        if ".txt" in file:
            time.sleep(0.2)
            print(file)
            exists = True
    return exists

#encrypt a line using shifted dictionary
def encryptLine(word,dict):
    new = ""
    for letter in word:
        i = alph.index(letter)
        new+=(dict[i])
    return new

#use shifted dictionary to decrypt line
def decryptLine(word,dict):
    new = ""
    for letter in word:
        i = dict.index(letter)
        new+=alph[i]
    return new

#uses ascii value of password to generate shift amount
def passToShift(password):
    sum = 0
    for letter in password:
        sum += ord(letter)
    return sum%26 + 1

#generates alphabet shifted "shift" number of indexes
def dictionary(shift):
    new = []
    for i in range(len(alph)):
        idx = i + shift
        if idx > len(alph):
            idx = idx - len(alph)
        new.append(alph[idx-1])
    return new

#main encryption process -> opens file, encrypts, writes file
def encrypt():
    filename = input("Enter the name of the file you want to encrypt...(include .txt)\n")
    
    pw = getpass.getpass("Enter the desired password...")
    shift = passToShift(pw)
    dict = dictionary(shift)
    file = open(desktop + "/" + filename, "r")
    contents = file.readlines()
    
    newfilename = input("Enter the name of the new encrypted file...(include .txt)\n")
    newfile = open(desktop + "/" + newfilename,"w+")

    for line in contents:
        word = line.strip()
        newfile.write(encryptLine(word,dict)+ "\n")

    newfile.close()
    file.close()
    print("\n"+ "A new file has been created.\n")

#main decryption process -> opens file, decrypts, writes file
def decrypt():

    filename = input("Enter the name of the file you want to decrypt...(include .txt)\n")
    pw = getpass.getpass("Enter the password...")
    shift = passToShift(pw)
    dict = dictionary(shift)
    file = open(desktop + "/" + filename,"r")
    contents = file.readlines()

    newfilename = input("Enter the name of the newly decrypted file...(include.txt)\n")
    newfile = open(desktop + "/" + newfilename,"w+")
    
    for line in contents:
        word = line.strip()
        newfile.write(decryptLine(word,dict)+ "\n")
    newfile.close()
    file.close()
    print("\n"+ "A new file has been created.\n")

#prints title and desktop directory
print(intro)
time.sleep(2)
if printDirectory():
    print()
    #user input
    started = False
    while not started:
        choice = input("Would you like to encrypt or decrypt your file?\n").lower()
        if choice == "encrypt":
            started = True
            encrypt()
        elif choice == "decrypt":
            started = True
            decrypt()
        elif choice == "quit":
            exit()
        else:
            pass
else:
    print("There are no .txt files in the user's desktop directory. Exiting...")
    time.sleep(2)
    exit()
