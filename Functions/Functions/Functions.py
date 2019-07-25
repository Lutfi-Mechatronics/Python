


from os import system, name
import os

# For line 38
import msvcrt as m
def wait(): return m.getch()

# Defining a Function's function
def hello():
    print("First function started")
    print("hello")
    print("hello again!")

def getinteger():
    print("Multiplying 2 values together")
    num1=float(input("Enter First digit : "))
    num2=float(input("Enter second digit : "))

    result=num1*num2

    # return value to the function that calls this function getinteger()
    return result           

# Defining the main function
def main():
    print("started")
    hello()

    # will display "Please Enter to continue" before going to the next section
    os.system("pause") 
    
    # wait until ENTER is pressed BUT any other input will be shown
    #input("")  
    # wait until any button is press             
    #wait() 

    # when any button is pressed, clear screen
    system('cls')           

    value = getinteger()
    print("{0}{1}".format("The final multiplied value is : ", value))

#Calling the main function
main()



