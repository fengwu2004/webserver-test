from pymongo import MongoClient

_instance = None

class DatabaseMgr(object):

    @classmethod
    def instance(cls):

        global _instance

        if _instance is None:

            _instance = DatabaseMgr()

        return _instance
    
    def __init__(self):

        self.client = MongoClient()

        self.db = self.client["testfei"]
    
    @property
    def stocks(self):
        
        return self.db['stocks']