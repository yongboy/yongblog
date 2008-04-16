import os
from google.appengine.ext.webapp import template

import cgi
import datetime
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp

import pojo

class ReplyList(webapp.RequestHandler):
  def get(self,bid):
    
    replys = db.GqlQuery("SELECT * "
                            "FROM LogReply "
                            "WHERE upid = :1 "
                            "ORDER BY date DESC",bid)
    template_values = {
      'upid': bid,
      'replys': replys
    }

    path = os.path.join(os.path.dirname(__file__), 'template/replylist.html')
    self.response.out.write(template.render(path, template_values))

class AddReply(webapp.RequestHandler):    
  def post(self):
    reply = pojo.LogReply()
    reply.upid = self.request.get('upid')
    if users.get_current_user():
      reply.author = users.get_current_user()
    reply.url = self.request.get('url')
    reply.content = self.request.get('content')
    reply.put()
    self.redirect('/blog/'+reply.upid)
      

application = webapp.WSGIApplication([
  (r'/reply/list/(.*)', ReplyList),
  ('/reply/add',AddReply)
], debug=True)


def main():
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
