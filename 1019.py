# _*_coding:utf-8_*_
def rank(x):
    while len(x) < 4:
        x = '0' + x
    x = ''.join(sorted(x))
    return x
n = raw_input()
while len(n) < 4:
    n += '0'
k = n
while k != 6174:
    n = rank(str(k))
    m = n[::-1]
    k = int(m)-int(n)
    print '%04d - %04d = %04d' % (int(m), int(n), k)
    if k == 0:
        break
