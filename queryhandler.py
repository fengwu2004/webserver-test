import json
import tokenManager
from datetime import datetime
from storemgr import *

from RequestBaseManager import RequestBaseManager


class queryHandler(RequestBaseManager):

    def options(self, *args, **kwargs):

        self.set_status(204)

        self.finish()

    def post(self):

        data = json.loads(self.request.body.decode('utf-8'))

        token = data['token']

        if tokenManager.instance().checkToken(token) is not True:

            self.write({'success':0, 'msg':'token出错'})

            return

        try:
            start = datetime.strptime(data['start'], '%Y-%m-%d')

            end = datetime.strptime(data['end'], '%Y-%m-%d')

        except:

            self.write({'success': 0, 'msg': '查询条件不全或者格式错误'})

            return

        senddata = dict()

        senddata['success'] = 1

        senddata['data'] = queryStocks(start, end)

        self.write(senddata)