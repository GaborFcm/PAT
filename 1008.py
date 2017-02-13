# _*_ coding:utf-8 _*_
num = raw_input().split(' ')
number, M = int(num[0]), int(num[1])
A = raw_input().split(' ')

if M != 0:
    M %= number
    M = -M

for i in xrange(number):
    print A[i+M],
