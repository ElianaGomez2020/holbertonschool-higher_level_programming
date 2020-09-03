#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv)
    if arg == 0:
        print ('0')
    else:
        sum = 0
        for i in range(1, arg):
            sum += int(argv[i])
        print("{}".format(sum))
