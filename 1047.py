# _*_coding:utf-8_*_
number = input()
a = [0 for i in xrange(1001)]
for i in xrange(number):
    string = raw_input().split(' ')
    troops = string[0].split('-')
    a[int(troops[0])] += int(string[1])
champion = a.index(max(a))
print champion, a[champion]
