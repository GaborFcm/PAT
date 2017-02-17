# _*_ coding:utf-8 _*_
def find_num(x, y):
    d = ''
    if y in x:
        for i in x:
            if y == i:
                d += y
        return int(d)
    return 0
strings = raw_input().split(' ')
pa = find_num(strings[0], strings[1])
pb = find_num(strings[2], strings[3])
print pa+pb
