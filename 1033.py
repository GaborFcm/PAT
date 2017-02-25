# _*_coding:utf-8_*_     # running out off time
bad_key = raw_input()
right_str = raw_input()
right_list = list(right_str)
for i in right_str:
    if '+' in bad_key and  ord(i)<=90 and ord(i)>=65:
        right_list.remove(i)
        continue
    if i.upper() in bad_key:
        right_list.remove(i)
print ''.join(right_list)


