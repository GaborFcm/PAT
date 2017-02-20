# _*_ coding:utf-8 _*_
right_str = raw_input()
wrong_str = raw_input()
lack_str = ''
for i in right_str:
    if i not in wrong_str and i.upper() not in lack_str:
        lack_str += i.upper()
print lack_str

