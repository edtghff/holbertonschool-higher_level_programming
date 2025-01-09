#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i != j:
            num = i * 10 + j
            if num == 89:
                print("{:02}".format(num))
            else:
                print("{:02}".format(num), end=", ")
