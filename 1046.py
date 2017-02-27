# _*_coding:utf-8_*_
number = input()
scores = [0, 0]
for i in xrange(number):
    string = raw_input().split(' ')
    digits = map(int, string)
    if digits[0]+digits[2] == digits[1] and digits[0]+digits[2] != digits[3]:
        scores[1] += 1
    elif digits[0]+digits[2] == digits[3] and digits[0]+digits[2] != digits[1]:
        scores[0] += 1
print scores[0], scores[1]

