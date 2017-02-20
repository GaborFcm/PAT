# _*_coding:utf-8_*_
times = raw_input().split(' ')
c1, c2 = int(times[0]), int(times[1])
clk_tck = 100
time = (c2-c1)/100.0
hour = int(time/3600)
minute = int(time % 3600/60)
second = int(round(time % 3600 % 60))
print '%02d:%02d:%02d' % (hour, minute, second)

