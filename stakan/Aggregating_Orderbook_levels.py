# уровень цен - накопленный объём на этом уровне цен
import pandas as pd
import requests
import math
from decimal import Decimal # решение проблемы плавающей запятой

symbol = 'SOLUSDT'
url = f'https://api.binance.com/api/v3/depth' # адрес для получения книги заказов вначале
interval = Decimal('0.1')

params = {
    'symbol':symbol,
    'limit': 100,
}

data = requests.get(url,params).json()

bid_levels = pd.DataFrame(data['bids'],columns=['price','quantity'],dtype=float)
min_bid_level = math.floor(min(bid_levels.price) / float(interval))*interval
max_bid_level = (math.ceil(max(bid_levels.price) / float(interval))+1)*interval
print(min_bid_level)
print(max_bid_level)











































































