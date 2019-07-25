from os import system, name
import os

#import msvcrt as m
#def wait(): return m.getch()


def forloops():
    # For Loop regarding values
    print("demonstration of For Loops")
    for step in range(5):
        print(step+1)

    # For Loop regarding a list of names
    words=["cat", "bat", "hat", "rat", "sat"]
    for word in words:
        print(word)

    fruits = ['banana', 'apple',  'mango', 'pear', 'papaya']
    for index in range(len(fruits)):
        if index < 5:
            print('Current fruit :', fruits[index])
            if fruits[index] == "pear":
                print("{0}{1}{2}".format("We found pear being ", index+1, "th."))
                break

def whileloop():
    num=0
    while num <= 0:
        num=float(input("Please enter a positive number : "))

def nestedwhileloop():
    i = 2
    while(i < 100):
       j = 2
       while(j <= (i/j)):
          if not(i%j): break
          j = j + 1
       if (j > i/j) : print(i, " is prime")
       i = i + 1

    print("Good bye!")



def main():
    forloops()
    os.system("pause")
    system("cls")
    whileloop()
    os.system("pause")
    system("cls")
    nestedwhileloop()

main()