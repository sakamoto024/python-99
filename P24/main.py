import random

#def rnd_select(a,b):
#    result = []
#    for i in range(a):
#        result.append(random.choice((range(b+1))))

#    return result

    #return [random.choice(range(b+1)) for i in range(a)]

################################修正コード##################################

def rnd_select(select_num,list_num):
    list_num = [i for i in range(list_num + 1)]
    ret = []

    for i in range(select_num):
        temp = random.choice(list_num)
        ret.append(temp)
        list_num.remove(temp)

    return ret
