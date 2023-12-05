#!/usr/bin/python3
def multiple_returns(sentence):
    tuplee = ()
    if len(sentence) == 0:
        tuplee = 0, "None"
    else:
        tuplee = len(sentence), sentence[0]
    return tuplee
