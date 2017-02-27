# _*_coding:utf-8_*_
def arab_mars(x):
    if x >= 13:
        a = x/13
        b = x % 13
        if b == 0:
            return high[a-1]
        else:
            return high[a-1], single[b]
    else:
        return single[x]
def mars_arab(x, size=1):
    if size == 1:
        return single.index(x)
    elif size == 3:
        return (high.index(x)+1)*13
    else:
        return (high.index(x[0])+1)*13+single.index(x[1])
display = []
single = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
high = ['tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
number = input()
for i in xrange(number):
    string = raw_input()
    if len(string) > 3:
        if string == 'tret':
            display.append(0)
        else:
            string = string.split(' ')
            display.append(mars_arab(string, 2))
    elif string in single:
        display.append(mars_arab(string))
    elif string in high:
        display.append(mars_arab(string, 3))
    else:
        display.append(arab_mars(int(string)))
for i in display:
    if len(str(i)) > 3:
        if i == 'tret':
            print i
        else:
            print i[0], i[1]
    else:
        print i
