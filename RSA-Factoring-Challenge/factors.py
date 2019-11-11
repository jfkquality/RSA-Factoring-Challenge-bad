#!/env/bin/python3
# Factorize all the things

import sys

with open(sys.argv[1]) as fp:

    arg = fp.readline()
    while arg != None:
        for i in range(2, int(arg) // 2):
            if (int(arg) % i == 0):
                print("{}={}*{}".format(int(arg), i, int(arg) // i))
                break
        arg = fp.readline()
