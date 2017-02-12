# _*_ coding:utf-8 _*_
import math
number = input()
def prime_number(x):
    j = 0
    end_num = int(math.sqrt(x))
    for i in xrange(2, end_num+1):
        if x % i == 0:
            break
        else:
            j = i
    if j == end_num:
        return x
    else:
        return 1

prime_num, count = [], 0
if number > 4:
    prime_num = [2, 3]
    for z in xrange(5, number+1, 2):
        prime_num.append(prime_number(z))
    prime_num = list(set(prime_num))
    if 1 in prime_num:
        prime_num.remove(1)
    prime_num.sort()
    for k in xrange(len(prime_num)-1):
        if prime_num[k+1] - prime_num[k] == 2:
            count += 1
print count
