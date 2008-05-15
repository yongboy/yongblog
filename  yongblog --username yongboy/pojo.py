from google.appengine.ext import db

class Greeting(db.Model):
  author = db.UserProperty()
  title = db.StringProperty()
  tags = db.StringListProperty(default=None)
  content = db.TextProperty()
  date = db.DateTimeProperty(auto_now_add=True)
  content_converted = db.TextProperty()

class LogReply(db.Model):
  upid = db.StringProperty()
  author = db.UserProperty()
  url = db.StringProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)
