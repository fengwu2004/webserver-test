from RequestBaseManager import RequestBaseManager
from io import BytesIO
from datetime import datetime
from stock import Stock
from openpyxl import load_workbook
import storemgr

def getItems(ws) -> set:
    
    results = set()
    
    for i in range(1, ws.max_row):
    
        obj = Stock()
        
        index = str(i + 1)

        obj.stockId = ws['A' + index].value
        
        temp = str(ws['B' + index].value)
        
        obj.datestr = datetime.strptime(temp[0:10], '%Y/%m/%d').strftime('%Y/%m/%d')

        obj = str(ws['C' + index].value)

        results.add(obj)
        
    return results

class SaveStocks(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = self.request.files['upload'][0].body

        wb = load_workbook(filename = BytesIO(data))
        
        ws = wb.active
        
        storemgr.saveStocks(getItems(ws))

        self.write({'success': 1})