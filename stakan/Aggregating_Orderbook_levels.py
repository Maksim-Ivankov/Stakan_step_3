# уровень цен - накопленный объём на этом уровне цен
import pandas as pd
import requests
import math
from decimal import Decimal # решение проблемы плавающей запятой

symbol = 'STMXUSDT'
url = f'https://api.binance.com/api/v3/depth' # адрес для получения книги заказов вначале
interval = Decimal('0.000001')

params = {
    'symbol':symbol,
    'limit': 100,
}

data = requests.get(url,params).json()

# # борьба с плавающей точкой - 
# factor = data['bids'][0][0]
# precesion = len(factor.split('.')[-1])
# factor = 10**precesion

# bids = data['bids']
# bids = [ [X[0]]]

bid_levels = pd.DataFrame(data['bids'],columns=['price','quantity'],dtype=float)
bid_levels['side'] = 'bid'
min_bid_level = math.floor(min(bid_levels.price) / float(interval))*interval
max_bid_level = (math.ceil(max(bid_levels.price) / float(interval))+1)*interval

bid_level_bounds = [float(min_bid_level+interval*x) for x in range(int((max_bid_level-min_bid_level)/interval)+1)] # определяем чанки - уровни сжатия цены

bid_levels['bin'] = pd.cut(bid_levels.price, bins = bid_level_bounds,right=False,precision=10) # к какому чанку относится цена
bid_levels = bid_levels.groupby('bin').agg(quantity = ('quantity','sum'), side = ('side','first')).reset_index()
bid_levels['label'] = bid_levels.bin.apply(lambda X: X.left)
# print(bid_levels) # выше спреда


ask_levels = pd.DataFrame(data['asks'],columns=['price','quantity'],dtype=float)
ask_levels['side'] = 'ask'
min_ask_level = (math.floor(min(ask_levels.price) / float(interval))-1)*interval
max_ask_level = (math.ceil(max(ask_levels.price) / float(interval))+1)*interval

ask_level_bounds = [float(min_ask_level+interval*x) for x in range(int((max_ask_level-min_ask_level)/interval)+1)] # определяем чанки - уровни сжатия цены

ask_levels['bin'] = pd.cut(ask_levels.price, bins = ask_level_bounds,right=True,precision=10) # к какому чанку относится цена
ask_levels = ask_levels.groupby('bin').agg(quantity = ('quantity','sum'), side = ('side','first')).reset_index()
ask_levels['label'] = ask_levels.bin.apply(lambda X: X.right)

# print(ask_levels) # ниже спреда

orderbook = pd.concat([ask_levels,bid_levels])
orderbook = orderbook[orderbook.quantity>0]

print(orderbook.sort_values('label',ascending=False).to_string())

































































