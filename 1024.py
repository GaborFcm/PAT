# _*_coding:utf-8_*_
number = raw_input()    # 链表？
index_E = number.find('E')
index_point = number.find('.')
shift = int(number[index_E+2:])
if number[index_E+1] == '-':
    shift = -shift
a = len(number[index_point+1:index_E])
if shift < 0:
    new = '0.'+'0'*(-shift-1)+number[index_point-1]+number[index_point+1:index_E]
elif shift == 0:
    new = number[index_point-1:index_E]
elif shift >= a:
    new = number[index_point-1]+number[index_point+1:index_E]+'0'*(shift-a)
elif shift < a:
    new = number[index_point-1]+number[index_point+1:index_point+1+shift]+'.'+number[index_point+1+shift:index_E]
if number[0] == '-':
    new = '-'+new
print new
