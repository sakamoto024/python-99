def huffman(list1):

    list2 = (sorted(list1,key = lambda x :x[1],reverse = True))
    #[['a', 45], ['d', 16], ['b', 13], ['c', 12], ['e', 9], ['f', 5]]
    
    #[a,[[c,b],[[f,e],d]]]
    top_tree = [list2[0][0],[[list2[3][0],list2[2][0]],[[list2[5][0],list2[4][0]],list2[1][0]]]]
    ret = []#このリストに結果を入れていく
    leaf1 = []#以下は葉の部分
    leaf2 = []
    leaf3 = []
    leaf4 = []

    for i,y in enumerate(top_tree):
        if i == 0:
            ret += [[y,str(i)]]
        else:
            leaf1 += y,str(i)
            #---------------------------------------------
            #ret =  [['a','0']]
            #leaf1 = [[['c', 'b'], [['f', 'e'], 'd']], '1']
            #---------------------------------------------

    #<leaf1について>

    for i,y in enumerate(leaf1[0]):
        if i == 0:
            leaf2 += y,str(i)
        else:
            leaf3 += y,str(i)
            #---------------------------------------------
            #leaf2 = [['c', 'b'], '0']
            #leaf3 = [[['f', 'e'], 'd'], '1']
            #---------------------------------------------

    #<leaf2について>
    for i,y in enumerate(leaf2[0]):
        ret.append([y,leaf1[1] + leaf2[1] + str(i)])
        #ret = [['a', 0], ['c', '100'], ['b', '101']]

    #<leaf3について>
    for i,y in enumerate(leaf3[0]):
        if i == 0:
            leaf4 += y,str(i)
        else:
            ret.append([y,leaf1[1] + leaf3[1] + str(i)])
            #-----------------------------------------------
            #leaf4 = [['f', 'e'], '0']
            #ret =[['a', '0'], ['c', '100'], ['b', '101'], ['d', '111']]
            #-----------------------------------------------
    
    #<leaf4について>
    for i,y in enumerate(leaf4[0]):
        if i == 0:
            ret.append([y,leaf1[1] + leaf3[1] + leaf4[1] + str(i)])
        else:
            ret.append([y,leaf1[1] + leaf3[1] + leaf4[1] + str(i)])

    ret = sorted(ret,key = lambda x :x[0])
    

    return ret
