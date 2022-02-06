"""class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="%s">link to story 1</a>' %
                   self.reverse_url("story", "1"))

class StoryHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self, story_id):
        self.write("this is story %s" % story_id)"""




        

"""class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="%s">link to story 1</a>' %
                   self.reverse_url("story", "1"))

class StoryHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self, story_id):
        self.write("this is story %s" % story_id)

app = tornado.web.Application([
    tornado.web.url(r"/", MainHandler),
    tornado.web.url(r"/story/([0-9]+)", StoryHandler, "db", name="story")
    ],debug=True)
app.listen(3000)
tornado.ioloop.IOLoop.current().start()"""