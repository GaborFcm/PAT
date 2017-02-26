# _*_coding:utf-8_*_
string = raw_input()
PAT = 'PATest'
numbers = [0 for i in xrange(6)]
for i in string:
    if i in PAT:
        numbers[PAT.find(i)] += 1
new_string = ''
a = sum(numbers)
while a > 0:
    if numbers[0] > 0:
        new_string += 'P'
        numbers[0] -= 1
        a -= 1
    if numbers[1] > 0:
        new_string += 'A'
        numbers[1] -= 1
        a -= 1
    if numbers[2] > 0:
        new_string += 'T'
        numbers[2] -= 1
        a -= 1
    if numbers[3] > 0:
        new_string += 'e'
        numbers[3] -= 1
        a -= 1
    if numbers[4] > 0:
        new_string += 's'
        numbers[4] -= 1
        a -= 1
    if numbers[5] > 0:
        new_string += 't'
        numbers[5] -= 1
        a -= 1
print new_string
