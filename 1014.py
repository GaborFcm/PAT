# _*_　coding:utf-8 _*_
def same_str(x, y, mark=False, s=None):
    z = []
    for i in xrange(min(len(x), len(y))):
        if x[i] == y[i]:
            z.append(x[i])
            if mark and x[i].upper() in s:
                return i
    return z

strings = []
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
AtoZ = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for j in xrange(4):
    strings.append(raw_input())
same = same_str(strings[0], strings[1])
for j in xrange(len(same)):
    if same[j] in AtoZ[10:17]:
        position = AtoZ[10:17].find(same[j])
        for k in xrange(j+1, len(same)):
            if same[k] in AtoZ[:24]:
                position1 = AtoZ[:24].find(same[k])
                break
        break
position2 = same_str(strings[2], strings[3], True, AtoZ[10:])

print '%s %02d:%02d' % (week[position], position1, position2)

