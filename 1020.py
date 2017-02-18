# _*_coding:utf-8_*_
demand = raw_input().split(' ')
stock = raw_input().split(' ')
sell_price = raw_input().split(' ')
demand = map(int, demand)
stock = map(float, stock)       # 存储量和总价格都是正数
sell_price = map(float, sell_price)
price, index = [], []
for i in xrange(len(stock)):
    price.append(sell_price[i] / stock[i])
x = reversed(sorted(price))
for i in x:
    index.append(price.index(i))
j, profit = 0, 0
if sum(stock) <= demand[1]:   # 供不应求
    profit = sum(sell_price)
else:
    while demand[1] > 0:
        if stock[index[j]] < demand[1]:
            profit += sell_price[index[j]]
        else:
            profit += price[index[j]]*demand[1]
            break
        demand[1] -= stock[index[j]]
        j += 1

print '%.2f' % profit
