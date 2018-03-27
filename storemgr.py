from datetime import datetime

from stock import Stock
from databasemgr import DatabaseMgr
from typing import Dict
import tushare as ts


def saveStocks(stocks: set):

    reuslts = list(map(lambda item: item.toJson(), stocks))

    DatabaseMgr.instance().stocks.remove({})

    DatabaseMgr.instance().stocks.insert_many(reuslts)

