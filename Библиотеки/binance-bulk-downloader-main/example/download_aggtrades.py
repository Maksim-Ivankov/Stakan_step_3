# import binance_bulk_downloader
from binance_bulk_downloader.downloader import BinanceBulkDownloader

# сгенерировать экземпляр
downloader = BinanceBulkDownloader(data_type="aggTrades")

# скачать aggredes (актив="um")
downloader.run_download()

# загружать ежемесячные отчеты (timeperiod_per_file="ежемесячно")
downloader = BinanceBulkDownloader(data_type="aggTrades", timeperiod_per_file="monthly")
downloader.run_download()

# скачать aggredes (asset="cm")
downloader = BinanceBulkDownloader(data_type="aggTrades", asset="cm")
downloader.run_download()

# загружайте ежемесячные отчеты о прибылях и убытках (asset="cm", timeperiod_per_file="ежемесячно")
downloader = BinanceBulkDownloader(
    data_type="aggTrades", asset="cm", timeperiod_per_file="monthly"
)
downloader.run_download()
