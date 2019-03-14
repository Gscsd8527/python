import tornado.web
import tornado.ioloop
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self, *args, **kwargs):
        """对应http的get请求方式"""
        stu = {
            "name": "zhangsan",
            "age": 24,
            "gender": 1,
        }
        self.write(stu)
if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', IndexHandler),

    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

