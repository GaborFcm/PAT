# _*_ coding:utf-8 _*_
num = raw_input().split(' ')
number, M = int(num[0]), int(num[1])
A = raw_input().split(' ')
M %= number
for i in xrange(M):
    b = A[-1]
    A[1:] = A[:-1]
    A[0] = b
for i in A:
    print i,

