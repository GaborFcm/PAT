# _*_coding:utf-8_*_
string = raw_input()
a = [0 for i in xrange(26)]
for i in string:
    b = ord(i.lower()) - 97
    if b >= 0 and b <= 25:
        a[b] += 1
c = max(a)
for i in xrange(26):
    if a[i] == c:
        print chr(i+97), c
        break
