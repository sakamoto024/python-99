
def combination(size,x,index=0,temp=[]):
    ret = []
    for i in range(index, len(x)):
        add = temp + [x[i]]
        #print(add)
        #[1]
        #[1, 2] 再帰処理
        #[1, 3] 再帰処理
        #[1, 4] 再帰処理
        #[1, 5] 再帰処理
        #[2]　　元のループに戻ってくる
        #[2, 3] 再帰
        #[2, 4] 〃
        #[2, 5] 〃
        #[3]　　元のループ
        #[3, 4] 再帰
        #[3, 5] 〃
        #[4]    元のループ
        #[4, 5] 再帰
        #[5]　　元のループ
        #[[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]


        if len(add) == size:
            ret = ret + [add]
        elif len(add) < size:
            ret = ret + combination(size, x, i + 1, add)
            #再帰処理を行っている。
            #この時のaddは[1]。
            #ret = [] + combination(size→2,x→[1,2,3,4,5],index→0+1,temp→[1])
            #
            #for i in range(1,5):
            #    add = [1] + [x[1]]→2
            #    add = [1,2]
            #そのままループのiに2が代入された処理に進む。


    return ret

##########################組み込み関数combinationsを使用した場合######################
#def combination(size,x):
#    ret = []
#    temp = combinaitons(int_list,int_split)#下記重複なしの組み合わせができる。
#    for i in temp:
#    print(i)
#      (1, 2)
#      (1, 3)
#      (1, 4)
#      (1, 5)
#      (2, 3)
#      (2, 4)
#      (2, 5)
#      (3, 4)
#      (3, 5)
#      (4, 5)

#    for i in temp:
#        result.append(list(i))

#    return result
