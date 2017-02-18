# _*_ coding:utf-8 _*_
num = raw_input()
numbers = {}
number = list(set(num))
for i in number:
    numbers[i] = 0
for i in num:
    numbers[i] += 1

for i in sorted(numbers.keys()):
    print '%s:%d' % (i, numbers[i])


