import sys
sys.path.append('../')
from P40.main import goldbach

def goldbach_list(lower_num,upper_num,limit_num = 0):
    even_list= []
    limit_list = []

    #偶数リスト作成
    for i in range(lower_num,upper_num+1):
        if i % 2 == 0 and i > 2:#2よりも小さいものははじく
            even_list.append([i])

    count = 0

    #以下limit_numに値が代入されないときのリストを作る
    while count <= len(even_list)-1:
            even_list[count] += goldbach(even_list[count][0])
            count += 1

    #以下limit_numよりも素数が大きいとき
    if limit_num > 0:
        for y in range(len(even_list)):
              #
              #even_list[y][1]&[2]→素数部分
              #
            if even_list[y][1] > limit_num and even_list[y][2] > limit_num:
                limit_list += [[even_list[y][0],even_list[y][1],even_list[y][2]]]
        return limit_list
    else:
        return even_list
