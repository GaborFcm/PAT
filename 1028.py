# _*_coding:utf-8_*_
number = input()            # running out of time
member = {}
today = 20140906
for i in xrange(number):
    string = raw_input().split(' ')
    birthday = string[1].split('/')
    birthday = ''.join(birthday)
    if 0 <= today - int(birthday) <= 2000000:
        member[string[0]] = today - int(birthday)
value = member.values()
if len(value) == 0:
    print 0
else:
    age_max, age_min = max(value), min(value)
    name_max, name_min = '', ''
    for i in member.keys():
        if member[i] == age_max:
            name_max = i
        if member[i] == age_min:
            name_min = i

    print len(value), name_max, name_min


