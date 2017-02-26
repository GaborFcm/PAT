# _*_coding:utf-8_*_
string = raw_input().split(' ')
P, A = string[0].split('.'), string[1].split('.')
P, A = map(int, P), map(int, A)
weight = [17*29, 29]
sum1 = P[0]*weight[0] + P[1]*weight[1] + P[2]
sum2 = A[0]*weight[0] + A[1]*weight[1] + A[2]
sum3 = sum2 - sum1
if sum3 < 0:
    sum3 = -sum3
    print '-%d.%d.%d' % (sum3/weight[0], sum3%weight[0]/weight[1], sum3%weight[0]%weight[1])
else:
    print '%d.%d.%d' % (sum3/weight[0], sum3%weight[0]/weight[1], sum3%weight[0]%weight[1])