#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_return = ()
    if sentence:
        tuple_return = len(sentence), sentence[0]
        return tuple_return
