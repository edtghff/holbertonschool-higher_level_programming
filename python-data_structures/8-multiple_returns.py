#!/usr/bin/python3
def multiple_returns(sentence):
    legth = 0
    for i in sentence:
        legth += 1

    if legth != 0:
        return legth, sentence[0]
    else:
        return legth, "None"
