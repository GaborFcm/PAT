# _*_ coding:utf-8 _*_
times = input()
A, B, C = [0, 0, 0], 0, [0, 0, 0]
index = ['B', 'C', 'J']
for i in xrange(times):
    gesture = raw_input().split(' ')
    if gesture[0] == gesture[1]:
        B += 1
    elif gesture[0] == 'C' and gesture[1] == 'J':
        A[1] += 1
    elif gesture[0] == 'C' and gesture[1] == 'B':
        C[0] += 1
    elif gesture[0] == 'J' and gesture[1] == 'C':
        C[1] += 1
    elif gesture[0] == 'J' and gesture[1] == 'B':
        A[2] += 1
    elif gesture[0] == 'B' and gesture[1] == 'J':
        C[2] += 1
    else:
        A[0] += 1

print sum(A), B, sum(C)
print sum(C), B, sum(A)
print index[A.index(max(A))], index[C.index(max(C))]
