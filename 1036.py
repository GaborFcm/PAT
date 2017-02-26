# _*_coding:utf-8_*_
string = raw_input().split(' ')
n, c = int(string[0]), string[1]
m = int(round(n*0.5))
for i in xrange(m):
    if i == 0 or i == m-1:
        print c*n
    else:
        print c+' '*(n-2)+c



