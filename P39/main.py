def prime_numbers( int1, int2):
    ret = []

    #先にリストを作る
    if int2 > 0:
        int3 = [i for i in range(int1,int2+1)]
    else:
        int3 = [i for i in range(int2,int1+1,1)]

    for i in int3:
        for y in range(2,len(int3)):
            if i < 0 or i == 0 or i == 1:#マイナスで始まるものはここではじく
                break
            elif i % y == 0 and i != y:
                break
        else:
            ret.append(i)

    return ret
