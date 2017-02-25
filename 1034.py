# _*_coding:utf-8_*_         # one wrong test can't pass
import sys
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)
def translate(x):
    a = x.split('/')
    m, n = abs(long(a[0])), abs(long(a[1]))
    if n == 0:
        return 'Inf'
    b = m % n
    c = m/n
    if b == 0:
        count = str(c)
    elif c == 0:
        count = '%Ld/%Ld' % (m, n)
    else:
        count = str(c)
        d = '%Ld/%Ld' % (m-c*n, n)
        count = count + ' ' + d
    if float(a[0])/float(a[1]) < 0:
        return '('+'-'+count+')'
    else:
        return count
string = raw_input().split()
dividend = translate(string[0])
divisor = translate(string[1])
sign = ['+', '-', '*', '/']
m = string[0].split('/')
a, b = long(m[0]), long(m[1])
n = string[1].split('/')
c, d = long(n[0]), long(n[1])

mole, denom = a*d+c*b, b*d
common = gcd(mole, denom)
mole, denom = mole/common, denom/common
x = '%d/%d' % (mole, denom)
print dividend, '+', divisor, '=', translate(x)

mole, denom = a*d-c*b, b*d
common = gcd(mole, denom)
mole, denom = mole/common, denom/common
x = '%Ld/%Ld' % (mole, denom)
print dividend, '-', divisor, '=', translate(x)

mole, denom = a*c, b*d
common = gcd(mole, denom)
mole, denom = mole/common, denom/common
x = '%Ld/%Ld' % (mole, denom)
print dividend, '*', divisor, '=', translate(x)
if c == 0:
    print dividend, '/', divisor, '=', 'Inf'
else:
    mole, denom = a*d, b*c
    common = gcd(mole, denom)
    mole, denom = mole/common, denom/common
    x = '%Ld/%Ld' % (mole, denom)
    print dividend, '/', divisor, '=', translate(x)
