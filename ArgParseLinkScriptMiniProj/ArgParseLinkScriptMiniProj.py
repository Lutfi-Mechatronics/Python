


import argparse
import math
import mathFunctionModule as func

helpDescribe = ["Add 2 numbers together",
                   "Subtract first number by second",
                   "Multiply first number by second",
                   "Devide first number by second",
                   "x^y",
                   "Display only the equation",
                   "Display output in sentences",
                   "First number",
                   "second number"]

variableParser = argparse.ArgumentParser(
    description = "Mathematical Operations on 2 numbers x and y")

mathFunction = variableParser.add_mutually_exclusive_group()
verbosity = variableParser.add_mutually_exclusive_group()

mathFunction.add_argument("-A", "--add", help = helpDescribe[0], 
                    action = "store_true")
mathFunction.add_argument("-S", "--subtract", help = helpDescribe[1], 
                    action = "store_true")
mathFunction.add_argument("-M", "--multiply", help = helpDescribe[2], 
                    action = "store_true")
mathFunction.add_argument("-D", "--devide", help = helpDescribe[3], 
                    action = "store_true")
mathFunction.add_argument("-E", "--exponent", help = helpDescribe[4], 
                    action = "store_true")

verbosity.add_argument("-Q", "--quiet", help = helpDescribe[5], 
                    action = "store_true")
verbosity.add_argument("-V", "--verbose", help = helpDescribe[6], 
                    action = "store_true")


variableParser.add_argument("x", type = float, help = helpDescribe[7])
variableParser.add_argument("y", type = float, help = helpDescribe[8])


arguments = variableParser.parse_args()

if arguments.add:
    func.add(arguments.x,arguments.y,arguments)

elif arguments.subtract:
    func.subtract(arguments.x,arguments.y,arguments)

elif arguments.multiply:
    func.multiply(arguments.x,arguments.y,arguments)

elif arguments.devide:
    func.devide(arguments.x,arguments.y,arguments)

elif arguments.exponent:
    func.exponent(arguments.x,arguments.y,arguments)