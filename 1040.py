# _*_coding:utf-8_*_
def numbers_pt(x, y):   # running time out of
    n, m = 0, 0
    for i in x:
        if i == 'P':
            n += 1
    for j in y:
        if j == 'T':
            m += 1
    return n, m
PAT = raw_input()
num = 0
index = []
for i in xrange(len(PAT)):
    if PAT[i] == 'A':
        index.append(i)
count = 0
for i in xrange(len(index)):
    n, m = numbers_pt(PAT[:index[i]], PAT[index[i]:])
    count += n*m
print count % 1000000007

