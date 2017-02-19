# _*_coding:utf-8_*_
listing = raw_input().split(' ')
boole = True
z, start = '', ''
for i in xrange(10):
    if listing[i] != '0':
        if i != 0 and boole:
            start = str(i)
            boole = False
            listing[i] = str(int(listing[i])-1)
        z += str(i)*int(listing[i])

print start+z
