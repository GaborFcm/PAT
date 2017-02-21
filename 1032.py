# _*_coding:utf-8_*_
number = input()                   # running out off time
a = [0 for i in xrange(100000)]
for i in xrange(number):
    string = raw_input().split(' ')
    string = map(int, string)
    a[string[0]] += string[1]
print a.index(max(a)), max(a)


