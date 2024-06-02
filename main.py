# pip install git+https://github.com/aoki-h-jp/binance-bulk-downloader
# Все качается отсюда - https://data.binance.vision/?prefix=data/futures/cm/daily/

from binance_bulk_downloader.downloader import BinanceBulkDownloader

# Загрузите все данные aggTrades (фьючерсы на USDT-M)
downloader = BinanceBulkDownloader(data_type='aggTrades')
downloader.run_download()




