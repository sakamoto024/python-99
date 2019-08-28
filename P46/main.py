from itertools import product


def AND(a,b):
    return a and b

def OR(a,b):
    return a or b

def NAND(a,b):
    return not a or not b

def NOR(a,b):
    return not a and not b

def XOR(a,b):
    return a != b

def IMP(a,b):
    return a == b or not a

def EQ(a,b):
    return a == b


def table(lamb):
    ret = lamb
    table = []

    for a, b in product([True, False], repeat=2):
    # print(a, b)
    # True True
    # True False
    # False True
    # False False
        table.append([a, b, ret(a, b)])

    return table
