#!/env/bin/python3
# Factorize all the things

import sys

with open(sys.argv[1]) as fp:

    arg = fp.readline()
    while arg:
        for i in range(2, arg/2):
            if (arg % i == 0):
                print("{}={}*{}".format(arg, i, arg/i)
                # break
        arg = fp.readline()
