

import argparse
import math

parserOne = argparse.ArgumentParser(description = "calculates exponent : X ^ Y")

group = parserOne.add_mutually_exclusive_group()
group.add_argument("-V","--verbosity", help = "increase verbosity output", 
                    action = "store_true")
group.add_argument("-Q","--quiet", help = "decrease verbosity output", 
                    action = "store_true")

parserOne.add_argument("x", type = int, help = "base")
parserOne.add_argument("y", type = int, help = "exponent")

args = parserOne.parse_args()
ans = args.x**args.y

if args.verbosity:
    print("{0} to the power of {1} is {2}".format(args.x, args.y, ans))

elif args.quiet:
    print("{0} ^ {1} = {2}".format(args.x, args.y, ans))

else:
    print(ans)