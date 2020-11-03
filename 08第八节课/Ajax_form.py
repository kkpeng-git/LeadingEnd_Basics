import tornado.ioloop
import tornado.web


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("Ajax_form.html")
#
#     def post(self, *args, **kwargs):
#         print(self.get_argument("user"))
#         print(self.get_argument("pwd"))
#         self.write("登陆成功")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("Ajax_jquery.html")

    def post(self, *args, **kwargs):
        a = int(self.get_argument("aa"))
        b = int(self.get_argument("bb"))
        c = a + b
        print(c)
        return_data = {"result": c}
        self.write(return_data)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
