#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    if argc == 1:
        print("{}".format(argc - 1))
    else:
        sumofarg = 0
        for x in range(1, argc):
            sumofarg += int(argv[x])
        print("{}".format(sumofarg))
