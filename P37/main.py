import sys
sys.path.append('../')
from P36.main import prime_factors_multi

def totient_phi(num):
    base = prime_factors_multi(num)
    formula = 0 #後ほど式を入れる

    for i in range(len(base)):
        if formula > 0:
            formula *= (base[i][0]-1) * base[i][0] ** (base[i][1]-1)
        else:
            formula = (base[i][0]-1) * base[i][0] ** (base[i][1]-1)
            
    return formula


##############################修正コード###################################
#def totient_phi(num):
#    for i,y in base:
#        if formula > 0:
#            formula *= (i-1) * i ** (y-1)
#        else:
#            formula = (i-1) * i ** (y-1)

#    return formula


#############################修正コードPart2###############################
#    import functools
#    import operator
#def totient_phi(num):
#    formula = list(map(lambda x: (x[0]-1) * x[0] ** (x[1]-1),base))
    
#    result = functools.reduce(operator.mul,formula)

#    return result
