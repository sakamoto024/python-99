def gray(n):
#グレイコードメモ
#半分で切ってみる
#00 01 | 11 10
#最下位ビットだけとる、0 1 | 1 0

#000 001 011 010 | 110 111 101 100
#0 1 1 0 | 0 1 1 0


    if n == 1:
        return ['0','1']

    gray_codes = gray(n-1)
    return [f'0{k}' for k in gray_codes] + [f'1{k}' for k in reversed(gray_codes)]
