# _*_ coding:utf-8 _*_
import math
number = input()
def is_prime(x):
    end_num = int(math.sqrt(x))
    for i in xrange(2, end_num+1):
        if x % i == 0:
            return False
    return True

z_pre, count = 2, 0
if number > 2:
    for z in xrange(3, number+1, 2):
        if is_prime(z):
            if z - z_pre == 2:
                count += 1
            z_pre = z
print count

