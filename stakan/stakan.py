
import asyncio
from websockets import connect
import aiofiles
import sys
import json
import httpx
from datetime import datetime
import time

# загружает книгу заказов, после чего получаем обновления в книге заказов
async def orferbook_download(pair):
    websocket_url = f'wss://stream.binance.com:9443/ws/{pair.lower()}@depth' # адрес для вебсокетов - обновление стакана
    rest_url = f'https://api.binance.com/api/v3/depth' # адрес для получения книги заказов вначале
    today = datetime.now().date()
    params = { # параметры для книги заказов
        'symbol':pair.upper(),
        'limit':100,
    }
    async with httpx.AsyncClient() as client: # получаем книгу заказов
        snapshot = await client.get(rest_url,params=params)
    snapshot = snapshot.json()
    snapshot['time'] = time.time()
    
    async with aiofiles.open(f'{pair.lower()}-snapshots-{today}.txt', mode = 'a') as f: # асинхронно сохраняет данные книги заказов в файл
        await f.write(json.dumps(snapshot)+'\n')
    

    async with connect(websocket_url) as websocket:
        while True:
            data = await websocket.recv() # записываем полученные данные в переменную
            print(data)

            async with aiofiles.open(f'{pair.lower()}-updates-{today}.txt', mode = 'a') as f: # асинхронно сохраняет данные обновления книги заказов в файл
                await f.write(data+'\n')


asyncio.run(orferbook_download('BTCUSDT')) # Запускаем асинхронные функции так
































































