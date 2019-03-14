import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello Itcast!")

class Hello(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("验证代码")

if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/',IndexHandler),
        (r'/hello',Hello),
    ])
http_server = tornado.httpserver.HTTPServer(app)
http_server.bind(8000)
http_server.start()
tornado.ioloop.IOLoop.instance().start()
# 上面和下面这两种方法皆可以
# app.listen(8000)
# tornado.ioloop.IOLoop.current().start()