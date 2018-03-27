class Stock(object):

    def __init__(self):

        self.stockId = ''

        self.datestr = ''

        self.increase = 0

    def toJson(self):

        return {
            'stockId':self.stockId,
            'datestr':self.datestr,
            'increase': self.increase
        }

    @classmethod
    def fromJson(cls, jsonvalue):

        obj = Stock()

        obj.stockId = jsonvalue['stockId']

        obj.datestr = jsonvalue['datestr']

        obj.increase = jsonvalue['increase']

        return obj