#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv)

    if len_argv == 1:
        print("{} arguments.".format(len_argv - 1))
    else:
        if len_argv == 2:
            print("{} argument:".format(len_argv - 1))
        else:
            print("{} arguments:".format(len_argv - 1))
        x = 1
        while x < len_argv:
            print("{}: {}".format(x, sys.argv[x]))
            x += 1
