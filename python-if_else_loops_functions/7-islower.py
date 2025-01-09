#!/usr/bin/python3
def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    elif ord('A') <= ord(c) <= ord('Z'):
        return False
