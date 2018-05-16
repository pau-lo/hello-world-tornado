import tornado.ioloop
import tornado.web


# route to index channel

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/home.html')

# self.write("Hello, world")

# r"/" == root website address
# where to find the static files , / root address


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)


# start the server as a port

if __name__ == "__main__":
    app = make_app()
    PortNumber = str(8888)
    print(r'App server now running.......')
    print(r'Server Running at http://localhost:' + PortNumber + r'/')
    print(r'To close press ctrl + c')
    app.listen(PortNumber)
    tornado.ioloop.IOLoop.current().start()
