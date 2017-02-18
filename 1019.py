# _*_coding:utf-8_*_
def rank(x):
    while len(x) < 4:
        x = '0' + x
    for i in xrange(len(x)):
        for j in xrange(i+1, len(x)):
            if int(x[i]) < int(x[j]):
                x = x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]

    return x
n = raw_input()
while len(n) < 4:
    n += '0'
k = n
while k != 6174:
    n = rank(str(k))
    m = n[::-1]
    k = int(n)-int(m)
    print '%04d - %04d = %04d' % (int(n), int(m), k)
    if k == 0:
        break
