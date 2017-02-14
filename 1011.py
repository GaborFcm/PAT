# _*_ coding:utf-8 _*_
times = input()
listing = []
for i in xrange(times):
    inputs = raw_input()
    inputs = inputs.split(' ')
    a, b, c = int(inputs[0]), int(inputs[1]), int(inputs[2])
    if a+b > c:
        listing.append('true')
    else:
        listing.append('false')

for i in xrange(len(listing)):
    print 'Case #%d: %s' % (i+1, listing[i])
