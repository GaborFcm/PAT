# _*_coding:utf-8_*_
string = raw_input().split(' ')
m, n = len(string[0]), len(string[1])
if m < n:
    string[0] = '0'*(n-m)+string[0]
elif m > n:
    string[1] = '0'*(m-n)+string[1]
a = map(int, list(string[0]))
b = map(int, list(string[1]))
a.reverse()
b.reverse()
d = ''
for i in xrange(len(a)):
    if i % 2 == 0:
        c = (a[i] + b[i]) % 13
        if c == 10:
            d += 'J'
        elif c == 11:
            d += 'Q'
        elif c == 12:
            d += 'K'
        else:
            d += str(c)
    if i % 2 == 1:
        c = b[i] - a[i]
        if c < 0:
            d += str(c+10)
        else:
            d += str(c)
d = list(d)
d.reverse()
d = ''.join(d)
print d
