# _*_ coding:utf-8 _*_
coefficient = raw_input().split()
coefficient = map(int, coefficient)

def derivation(a, b):
    return a*b, b-1

mark = False
for i in xrange(len(coefficient)/2):
    x, y = derivation(coefficient[2*i], coefficient[2*i+1])
    if x != 0:
        print x, y,
        mark = True
if not mark:
    print 0, 0,
