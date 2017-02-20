# _*_ coding:utf-8 _*_
command = raw_input().split(' ')
n = int(command[0])
num, k, residue = 1, 0, 0
while num <= n:
    k += 1
    num += 2*(k*2+1)
residue = n - num + 2*(k*2+1)
m = 2*k - 1
x = range(0, k)
for i in xrange(k-1):
    x.append(k-2-i)
for i in x:
    print i*' '+(m-2*i)*command[1]
print residue
