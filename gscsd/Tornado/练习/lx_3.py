import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define, options
from tornado.web import RequestHandler, url

tornado.options.define('port', type=int, default=8000, help="服务器端口")

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # subject = self.get_query_argument('subject')
        # subject = self.get_query_argument('subject', 'python')
        # query_args = self.get_query_arguments('q')  # 接收多个值http://127.0.0.1:8000/?q=1&q=2&q=3
        # body_args = self.get_body_arguments("b")
        # a = self.get_argument('a')
        f = self.request.files
        self.write('ok')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
