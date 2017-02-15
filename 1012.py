# _*_ coding:utf-8 _*_
numbers = raw_input().split(' ')
numbers = map(int, numbers)
A = ['N', 'N', 'N', 'N', 'N']
a = [0, 0, 0, 0, 0]
b, c, d = False, 0, 0
for i in xrange(1, len(numbers)):
    if numbers[i] % 10 == 0:
        a[0] += numbers[i]
    elif numbers[i] % 5 == 1:
        d += 1
        if not b:
            a[1] += numbers[i]
            b = True
        else:
            a[1] -= numbers[i]
            b = False
    elif numbers[i] % 5 == 2:
        a[2] += 1
    elif numbers[i] % 5 == 3:
        a[3] += numbers[i]
        c += 1
    elif numbers[i] % 5 == 4:  # cannot use "else" straight, use this constrain
        a[4] = max(a[4], numbers[i])

for i in xrange(len(a)):
    if a[i] != 0:
        A[i] = a[i]
    elif i == 1 and d != 0:    # a[1] may be equal 0 when A2 exists
        A[i] = a[i]
    if i == 3 and c != 0:
        A[3] /= float(c)
        print '%.1f' % A[i],
    else:
        print A[i],
