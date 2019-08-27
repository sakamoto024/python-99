def goldbach(num):
    #ゴールドバッハの予想は2より大きい偶数は2つの素数の和として表せる。
    prime_list = []
    ret = []
    #２以下の整数、または奇数は[]を返す。
    if num <= 2 or num % 2 != 0:
        return ret

    #numの素数をリスト化する
    for i in range(num+1):
        for y in range(2,num):
            if i == 1 or i == 0:
                break
            elif i % y == 0 and i != y:
                break
        else:
            prime_list.append(i)

    #和を出していく
    for  i in prime_list:
        for y in prime_list:
            if i + y == num:
                ret += [i,y]
                break
        else:
            continue
        break

    return ret
