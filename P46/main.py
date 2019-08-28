
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
    lamb2 = lamb
    table = []
    
    #True,Falseのすべての組み合わせを作成する
    temp = [[a,b] for a in [True,False] for b in [True,False]]

    for i in temp:
        table.append([i[0],i[1],lamb2(i[0],i[1])])

    return table


#######################組み込み関数productを使用した場合################
#from itertools import product

#    for a, b in: product([True, False], repeat=2):
    #print(a, b)
    # True True
    # True False
    # False True
    # False False

#        table.append([a, b, lamb2(a, b)])

#    return table
