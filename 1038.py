# _*_coding_*_  # running time out off
number = input()
scores = raw_input().split(' ')
string = raw_input().split(' ')
scores = map(int, scores)
string = map(int, string)
numbers = 0
n, stand = string[0], string[1:]
for i in xrange(n):
    numbers = 0
    for j in xrange(number):
        if stand[i] == scores[j]:
            numbers += 1
    print numbers,
