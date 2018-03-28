import tornado.escape
import tornado.ioloop
import tornado.web

from loginManager import loginManager
from save_upload_excel import SaveStocks
from queryhandler import queryHandler

def make_app():

    return tornado.web.Application([
        (r"/login", loginManager),
        (r"/upload", SaveStocks),
        (r"/query", queryHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()