import tornado.httpserver
import tornado.ioloop
import tornado.web
class IndexHandler(tornado.web.RequestHandler):
     def get(self):
         greeting = self.get_argument('greeting', 'Hello')
         self.write(greeting + ', friendly user!')
if __name__ == "__main__":

     app = tornado.web.Application(
          handlers=[(r"/", IndexHandler)]
 )
     http_server = tornado.httpserver.HTTPServer(app)
     http_server.listen(8000)
     tornado.ioloop.IOLoop.current().start()