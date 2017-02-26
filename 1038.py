# _*_coding_*_  # running time out off
number = input()
scores = [0 for i in xrange(101)]
a = raw_input().split(' ')
a = map(int, a)
for i in xrange(number):
    scores[a[i]] += 1
string = raw_input().split(' ')
string = map(int, string)
for i in string[1:]:
    print scores[i],

