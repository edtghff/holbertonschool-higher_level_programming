#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i == 9 and j == 9:
            print("{:02}".format(i * 10 + j))
        else:
            print("{:02}".format(i * 10 + j), end=", ")
