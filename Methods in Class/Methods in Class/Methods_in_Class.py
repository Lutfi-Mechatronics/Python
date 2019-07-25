

from os import system, name
import os
import math


class vector2d():
    x=0
    y=0

    def set(self, x, y):
        self.x=x
        self.y=y
def vector2d_function():
    vec=vector2d()
    vec.set(5.0,6.0)
    print("x : "+str(vec.x)+", Y : "+str(vec.y))

class secondvector2d():

    # __init__ initialise a and b as 0, Replacing set() method
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
def secondvector2d_function():
    vec = secondvector2d(5.258,6.365)
    print("x : "+str(vec.a)+", Y : "+str(vec.b))

class vector2dmath():

    def __init__(self, f, g):
        self.f=float(f)
        self.g=float(g)

    def __add__(self,other):
        return vector2dmath(self.f +other.f, self.g+other.g)
    def __iadd__(self, other):
        self.f += other.f
        self.g += other.g
        return self

    def __sub__(self,other):
        return vector2dmath(self.f - other.f,self.g - other.g)

    def __multiply__(self,other):
        return vector2dmath(self.f * other.f,self.g * other.g)
    def __imul__(self,other):
        self.f *= other.f
        self.g *= other.g
        return self

    def __truediv__(self, other):
        return vector2dmath(self.f/other.f, self.g/other.g)

    def getLength(self):
        return math.sqrt(self.f**2+self.g**2)
    def normalised(self):
        length = self.getLength()
        if length != 0:
            return vector2dmath(self.g/length, self.f/length)
        return vector2dmath(self)
    def getAngle(self):
        return math.degrees(math.atan2(self.f,self.g))
    def __str__(self):
        return "x : "+str(self.f)+"Y : "+str(self.g)  
def secondvector2d_math():
    vec = vector2dmath(5,6)
    vec2=vector2dmath(2,3)
    print(vec)
    print(vec2)

    vec=vec+vec2
    print(vec)

    vec+=4* vec2
    print(vec)

    vec = __add__.vector2dmath(2,2)
    print(vec)
    print(vec.normalised())
    print(vec.getAngle)


def pause():
    print("")
    system("pause")
    system('cls')

def select(selection):
    if selection == 1:
        system('cls')
        vector2d_function()
        pause()
        main()
    if selection == 2:
        system('cls')
        secondvector2d_function()
        pause()
        main()
    if selection == 3:
        system('cls')
        secondvector2d_math()
        pause()
        main()
    if selection == 4:
        SystemExit(0)
    if selection != 1 and selection !=2 and selection != 3 and selection != 4:
        system("cls")
        print("\n\nInvalid Input")
        pause()

def main():
    print("\n\nClass and Methods\n")
    print("1: Vector2D Sinple Output\n2: Special Method using __init__\n3: Vector 2D with"+
          " more added functionality Methods (Functions inside class)\n4: Exit")
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