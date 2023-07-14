#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    else:
        k = len(sentence)
        j = sentence[0]
        return (k, j)
