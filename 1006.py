# _*_ coding:utf-8 _*_
number = raw_input()
out0, out1, out2, out = '', '', '', ''
length = len(number)
if length >= 1:
    for i in xrange(int(number[-1])):
        out0 += str(i+1)
if length >= 2:
    for i in xrange(int(number[-2])):
        out1 += 'S'
if length >= 3:
    for i in xrange(int(number[-3])):
        out2 += 'B'
out = out2 + out1 + out0
print out
