from datetime import datetime

from stock import Stock
from databasemgr import DatabaseMgr
from typing import Dict
import tushare as ts


def saveStocks(stocks: set):

    reuslts = list(map(lambda item: item.toJson(), stocks))

    DatabaseMgr.instance().stocks.insert_many(reuslts)


def queryStocks(start:datetime, end:datetime):

    items = DatabaseMgr.instance().stocks.find({}, {'_id':0})

    results = []

    for item in items:

        stock = Stock.fromJson(item)

        if start <= datetime.strptime(stock.datestr, '%Y-%m-%d') <= end:

            results.append(stock)

    return [stock.toJson() for stock in results]

