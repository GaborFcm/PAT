# _*_coding:utf-8_*_
number = input()
string = raw_input().split()
digits = map(float, string)
sums = 0
for i in xrange(number):
    sums += (number-i)*(i+1)*digits[i]
print '%.2f' % sums

