# _*_ coding:utf-8 _*_
number = raw_input().split(' ')   # please take care of the title
number = map(int, number)
c = number[0] + number[1]
if c == 0:
    print 0
else:
    z = ''
    while c != 0:
        residue = str(c % number[2])
        z = residue + z
        c /= number[2]
    print z
