
from itertools import combinations

def group3(str_list):
    result_2 = []
    for i in combinations(str_list,2):
        for y in combinations(str_list[2:],3):
            for z in combinations(str_list[5:],4):
                result_2 += [[list(i),list(y),list(z)]]
    return result_2


def group(int_list,str_list,ls_1 = [],index = 0,result = None):
    if result is None:
        result = []
    if ls_1 is None:
        ls_1 = []

    if not str_list:#str_listが空になったときこのif文にひっかかる
        result.append(ls_1)
        return

    #ここで回すstr_listはソートしておかないといけない。
    #setのまま回すと順番が変わってしまう。例)[[b,a][d,e,c],[g,f,h]]
    for i in combinations(sorted(str_list),int_list[index]):
        ls_2 = ls_1.copy()
        ls_2.append(sorted(list(i)))
        str_list = set(str_list)
        group(int_list,str_list-set(i),ls_2,index + 1,result)#再帰処理
    
    return result
