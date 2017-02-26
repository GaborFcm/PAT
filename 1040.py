# _*_coding:utf-8_*_
PAT = raw_input()
num = 0
sum_T, sum_P, left_T = 0, 0, 0
for i in xrange(len(PAT)):
    if PAT[i] == 'T':
        sum_T += 1
count = 0
for i in PAT:
    if i == 'P':
        sum_P += 1
    elif i == 'A':
        count += sum_P*(sum_T - left_T)%1000000007
    else:
        left_T += 1
print count%1000000007

