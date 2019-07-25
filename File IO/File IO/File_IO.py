

from os import system, name
import os

def pause():
    print("")
    system("pause")
    system('cls')

def read():
    print("Reading File")

    #open("file_name.txt","r"
    # parameter "r" is to read the file.
    f=open("myfile.txt", "r")

    for line in f:
        print(line.strip("\n\r"))

    f.close()   # Close opened file

def write():
    print("Writing File")

    #open("file_name.txt","parameter"
    # parameter "w" is to write the file.
    f=open("myfile.txt", "w")
    for i in range(4):
        f.write(input("{0}{1}{2}".format("Please enter word ", i+1, " : "))+"\n")
    f.close()

def append():
    print("Append File")

    # open("file_name.txt","parameter")
    # parameter "a" is to add somthing new into the file.
    f=open("myfile.txt", "a")
    for i in range(4):
        f.write(input("{0}{1}{2}".format("Please enter word ", i+1, " : "))+"\n")
    f.close()

def select(selection):
    if selection == 1:
        system('cls')
        read()
        pause()
        main()
    if selection == 2:
        system('cls')
        read()
        pause()
        write()
        pause()
        read()
        pause()
        main()
    if selection == 3:
        system('cls')
        read()
        pause()
        append()
        pause()
        read()
        pause()
        main()
    if selection == 4:
        SystemExit(0)
    if selection != 1 and selection !=2 and selection != 3 and selection !=4:
        system("cls")
        print("\n\nInvalid Input")
        pause()
        main()

def main():

    selection = 0
    print("\n\nFile IO and Exceptions\n")
    print("1: Read Only\n2: Write\n3:Append\n4: Exit")
    selection=input("Enter Selection : ")
    try:
        selection = int(selection)
        select(selection)
    except ValueError:
        system("cls")
        print("\n\nInvalid Input Data Type\n")
        system("pause")
        system("cls")
        main()
main()