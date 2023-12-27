#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    if len(sentence) <= 0:
        print("Length: {:d} - First character: None".format(len(sentence)))
    print("Length: {:d} - First character: {:d}".format(len(sentence), first))
