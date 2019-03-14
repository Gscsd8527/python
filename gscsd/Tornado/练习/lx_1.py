import tornado.web
import tornado.ioloop
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self, *args, **kwargs):
        """对应http的get请求方式"""
        self.write('Hello Itcast! 1')
        # self.write('Hello Itcast! 2')
        # self.write('Hello Itcast! 3')
if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ])
    # app.listen(8000)
    # tornado.ioloop.IOLoop.current().start()

    # ------------------------------
    # 我们修改这个部分
    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    # ------------------------------
    tornado.ioloop.IOLoop.current().start()

    # 多线程方式
    # http_server = tornado.httpserver.HTTPServer(app)
    # # -----------修改----------------
    # http_server.bind(8000)
    # http_server.start(0)
    # # ------------------------------
    # tornado.ioloop.IOLoop.current().start()


    # -------------------------------
    # 最开始看tornado的启动方式
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.bind(8000)
    # http_server.start()
    # tornado.ioloop.IOLoop.instance().start()
