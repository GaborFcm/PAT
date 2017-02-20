# _*_coding:utf-8_*_    # running time out off
parameter = raw_input().split(' ')
array = raw_input().split(' ')
p = int(parameter[1])
array = map(int, array)
array.sort()
a = []
for j in xrange(len(array)):
    insert_a = array[j]*p
    if insert_a >= array[-1]:
        if j == 0:
            print len(array)
            break
        else:
            a.append(len(array)-j)
    elif insert_a < array[0]:
        print 0
        break
    else:
        for i in xrange(len(array)):
            if array[i] > insert_a:
                a.append(i-j)
                break
if len(a) > 0:
    print max(a)