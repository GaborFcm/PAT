# _*_ coding:utf-8 _*_
string = '0123456789'
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
M = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
def wrong_ID(x):
    for i in x:
        if i not in string:
            return True
    return False
def sum_weight(a):
    a = list(a)
    a = map(int, a)
    b = 0
    for i in xrange(len(a)):
        b += a[i]*weight[i]
    b %= 11
    return M[b]

number = input()
IDs = []
for j in xrange(number):
    ID = raw_input()
    if wrong_ID(ID[:-1]):
        IDs.append(ID)
        print ID
    elif sum_weight(ID[:-1]) != ID[-1]:
        IDs.append(ID)
        print ID
if len(IDs) == 0:
    print 'All passed'

