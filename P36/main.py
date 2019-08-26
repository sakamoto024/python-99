import sys
sys.path.append('../')
from P35.main import prime_factors

def prime_factors_multi(num):
    prime_list1 = prime_factors(num)
    #重複した要素を削除し、リストの順序を保持してリスト化する
    #setだと勝手に並び替えしてしまうので不向き。
    prime_list2 = list(dict.fromkeys(prime_list1))
    prime_count = []
    result = []

    #重複した素数の要素をカウント
    for i in prime_list2:
        prime_count.append(prime_list1.count(i))

    for prime_num,prime_count in zip(prime_list2,prime_count):
        result.append([prime_num,prime_count])

    return result




#####################【組み込み関数Counterを使った場合】###############################
#import sys                                                                           #
#sys.path.append('../')                                                               #
#from P35.main import prime_factors                                                   #
#from collections import Counter                                                      #
#                                                                                     #
#def prime_factors_multi(num):                                                        #
#    prime_list = prime_factors(num)                                                  #
#    prime_count = Counter(prime_list)                                                #
#    #print(prime_count)                                                              #
#    #Counter({3: 2, 5: 1, 2: 1})                                                     #
#    #キーに要素、値に出現回数をもつ辞書型のような形になる。                          　   #
#    result = []                                                                      #
#                                                                                     #
#    #キーと値をそれぞれ取り出して、サブリスト化                                          #
#    for primekey,primevalue in prime_count.items():                                  #
#　　    result.append([primekey,primevalue])                                         #
#                                                                                     #
#    return result                                                                    #
#######################################################################################
