import json
import tokenManager

from RequestBaseManager import RequestBaseManager


class loginManager(RequestBaseManager):
    
    def options(self, *args, **kwargs):
        
        self.set_status(204)
        
        self.finish()
    
    def post(self):

        data = json.loads(self.request.body.decode('utf-8'))

        username = data['name']

        password = data['pwd']

        msg = ''

        if username == 'yl' and password == 'yl0334':

            senddata = dict()

            senddata['success'] = 1

            senddata['msg'] = 'login success'

            senddata['token'] = tokenManager.instance().getToken(username)

            self.write(senddata)

            return

        senddata = dict()

        senddata['success'] = 0

        senddata['msg'] = 'login failed, 登陆名或密码错误'
        
        self.write(senddata)