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

    path = os.path.join(os.path.dirname(__file__), 'replylist.html')
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




class ViewBlog(webapp.RequestHandler):
  def get(self,bid):    
    greeting = db.get(bid)
    template_values = {
      'greeting': greeting,
      }

    path = os.path.join(os.path.dirname(__file__), 'viewblog.html')
    self.response.out.write(template.render(path, template_values))
    


#Anybody who had writed the blog has the right to edit it
class EditBlog(webapp.RequestHandler):
  def get(self,bid):
    if users.get_current_user() == None :
      self.redirect(users.create_login_url(self.request.uri))
      
    greeting = db.get(bid)
    if users.get_current_user() == greeting.author :
      template_values = {
        'greeting': greeting,
      }
      path = os.path.join(os.path.dirname(__file__), 'editblog.html')
      self.response.out.write(template.render(path, template_values))
    else :
      self.redirect("/exception/hasnoright.html")

#Anybody who had writed the blog has the right to update it
class UpdateBlog(webapp.RequestHandler):
  def post(self):
    if users.get_current_user() == None :
      self.redirect(users.create_login_url(self.request.uri))
      
    greeting = db.get(self.request.get('key'))
    if users.get_current_user() == greeting.author:
      greeting.title = self.request.get('title')
      greeting.content = self.request.get('content')
      
      greeting.put()
      self.redirect('/')
    else:
      self.redirect("/exception/hasnoright.html")
    
#Anybody who had writed the blog has the right to delete it
class DeleteBlog(webapp.RequestHandler):
  def get(self,bid):
    if users.get_current_user() == None :
      self.redirect("/exception/hasnoright.html")
      
    greeting = db.get(bid)
    if users.get_current_user() == greeting.author:
      greeting.delete()
      self.redirect('/')
    else :
      self.redirect("/exception/hasnoright.html")



      

application = webapp.WSGIApplication([
  (r'/reply/list/(.*)', ReplyList),
  ('/reply/add',AddReply)
], debug=True)


def main():
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
