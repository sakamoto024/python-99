
from itertools import product

def table(lamb):
    ls = []

    arg_num = lamb.__code__.co_argcount
    #ラムダ式.__code__.co_argcountでラムダ式の引数を取れるらしい。。

    for i in product([True,False],repeat = arg_num):
        ls.append(list(i)+[lamb(*i)])

    return ls
