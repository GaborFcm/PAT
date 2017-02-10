# _*_ coding:utf-8 _*_
def next_data(x):
    if x % 2 == 0:
        return x/2
    else:
        return (3*x+1)/2

n = input()
number = raw_input()
numbers = number.split(' ')
numbers = map(int, numbers)  # [int(i) for i in numbers]
for i in numbers:
    while i != 1:
        y = next_data(i)
        if y in numbers:
            numbers[numbers.index(y)] = 1
        i = y
numbers = list(set(numbers))
numbers.remove(1)
numbers.sort(reverse=True)
for i in numbers:
    print i,




