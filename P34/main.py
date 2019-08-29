#import sys
#sys.path.append('../')
#from P32.main import gcd

#def totient_phi(num):
#    count = 0
#    for i in range(1,num):
#        if gcd(i,num) == 1:
#            count += 1
#    return count


########################修正コード##########################
import sys
sys.path.append('../')
from P33.main import is_coprime

def totient_phi(num):
    count = 0
    for i in range(1,num):
        if is_coprime(i,num):
            count +=1
    return count
