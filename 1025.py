# _*_coding:utf-8_*_             # WRONG?
command = raw_input().split(' ')
n, m = int(command[1]), int(command[2])
listed, link = [], []
for i in xrange(n):
    listed.append(-1)
for i in xrange(n):
    number = raw_input().split(' ')
    listed[int(number[1])-1] = number[0]
for i in xrange(n/m):
    for j in xrange(m):
        link.append(listed[(i+1)*m-j-1])
if n % m != 0:
    for i in xrange(n % m):
        link.append(listed[n/m*m+i])
link.append(-1)
c = n/m*m
for i in xrange(n):
    if c > 0:
        print link[i], m*(i/m+1)-i%m, link[i+1]
    else:
        print link[i], i+1, link[i+1]
    c -= 1
