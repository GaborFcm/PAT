# _*_coding:utf-8_*_
number = input()
a = {}
for i in xrange(number):
    string = raw_input().split(' ')
    if string[0] not in a.keys():
        a[string[0]] = int(string[1])
    else:
        a[string[0]] += int(string[1])
score_max = max(a.values())
for i in a.keys():
    if score_max == a[i]:
        print i, score_max
        break

