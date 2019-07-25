
def add(a,b,arguments):
    c= a+b
    if arguments.quiet:
        print("{0}+{1}={2}".format(a,b,c))
    elif arguments.verbose:
        print("{0} add with {1} equals {2}".format(a,b,c))
    else:
        print(c)

    return 0;

def subtract(a,b,arguments):
    c = a - b
    if arguments.quiet:
        print("{0}-{1}={2}".format(a,b,c))
    elif arguments.verbose:
        print("{0} minus {1} equals {2}".format(a,b,c))
    else:
        print(c)
    
    return 0;

def multiply(a,b,arguments):
    c = a * b
    if arguments.quiet:
        print("{0} x {1}={2}".format(a,b,c))
    elif arguments.verbose:
        print("{0} multiply {1} equals {2}".format(a,b,c))
    else:
        print(c)
    
    return 0;

def devide(a,b,arguments):
    if b != 0:
        c = a / b
        if arguments.quiet:
            print("{0} / {1}={2}".format(a,b,c))
        elif arguments.verbose:
            print("{0} devide by {1} equals {2}".format(a,b,c))
        else:
            print(c)
    elif b == 0:
        if arguments.quiet:
            print("{0} / 0 = UNDEFINED".format(a))
        elif arguments.verbose:
            print("{0} devide  by 0 equals UNDEFINED".format(a))
        else:
            print("UNDEFINED")

    return 0;

def exponent(a,b,arguments):
    c = a ** b
    if arguments.quiet:
        print("{0} ^ {1}={2}".format(a,b,c))
    elif arguments.verbose:
        print("{0} to the power of {1} equals {2}".format(a,b,c))
    else:
        print(c)
    
    return 0;