# _*_ coding:utf-8 _*_
import math     # when m=1, n=10000 , exceeding time
import time
start = time.clock()
def isPrime(x):
    end = int(math.sqrt(x))+1
    for i in xrange(2, end):
        if x % i == 0:
            return False
    return True

primes, number = [2], 3
# numbers = raw_input().split(' ')
numbers = [1, 10000]
m, n = int(numbers[0]), int(numbers[1])
while n-1 >= 0:
    if isPrime(number):
        primes.append(number)
        n -= 1
    number += 2
count = 1
for j in xrange(m-1, int(numbers[1])):
    print primes[j],
    count += 1
    if count % 11 == 0:
        count = 1
        print
end = time.clock()
print end-start
