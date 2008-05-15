import os
import sys
from google.appengine.ext.webapp import template

import cgi
import datetime
import wsgiref.handlers
import logging

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp

import pojo
#sys.path.append('utils')


class MainPage(webapp.RequestHandler):
  def get(self):
    size = 10
    currpage = self.request.get('p')
    if currpage == '':
      currpage = '1'
    page = int(currpage)
    offset = (page-1)*size
    
    greetings = db.GqlQuery("SELECT * "
                            "FROM Greeting "
                            "ORDER BY date DESC")
    #Greeting.all().order('-date')

    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'

    nums =  greetings.count()

    pagestr = ''
    if page == 1 :
      if nums > size :
        pagestr = '<a href="/?p=' + str(page+1) + '">Next</a>'
      else :
        pagestr = '1'
    else :
      pagestr = '<a href="/?p='+str(page-1)+'">Pre</a>'
      if nums > size*page :
        pagestr += '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + ' <a href="/?p=' + str(page+1) + '">Next</a>'

    template_values = {
      'greetings': greetings.fetch(size,offset),
      'url': url,
      'url_linktext': url_linktext,
      'pagestr': pagestr,
      'curruser': users.get_current_user()
    }

    path = os.path.join(os.path.dirname(__file__), 'template/bloglist.html')
    self.response.out.write(template.render(path, template_values))



class ViewBlog(webapp.RequestHandler):
  def get(self,bid):    
    greeting = db.get(bid)

    replys = db.GqlQuery("SELECT * "
                            "FROM LogReply "
                            "WHERE upid = :1 "
                            "ORDER BY date DESC",bid)

    isCurruser = users.get_current_user() == greeting.author
    isAdmin = users.is_current_user_admin()

    logging.debug('isCurruser = %s' %  (isCurruser))
    logging.debug('isAdmin = %s' % (isAdmin))
    
    
    if isCurruser or isAdmin:
        isCanEdit = True
    else:
        isCanEdit = False

    template_values = {
      'greeting': greeting,
      'replys': replys,
      'isCanEdit': isCanEdit
    }

    path = os.path.join(os.path.dirname(__file__), 'template/viewblog.html')
    self.response.out.write(template.render(path, template_values))
    
# Anybody has the right to write blog~
class AddBlog(webapp.RequestHandler):
  def get(self):
    if users.get_current_user() == None :
      self.redirect(users.create_login_url(self.request.uri))
      
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'template/addblog.html')
    self.response.out.write(template.render(path, template_values))    
    
  def post(self):
    greeting = pojo.Greeting()
    if users.get_current_user():
      greeting.author = users.get_current_user()
      greeting.title = self.request.get('title')
      greeting.tags = self.request.get('tags').split(' ')
      content = self.request.get('content')
      greeting.content = content
      if content:
        greeting.content_converted = text2html(content)
      greeting.put()
      self.redirect('/')
    else :
      self.redirect("/exception/hasnoright.html")

#Anybody who had writed the blog has the right to edit it
class EditBlog(webapp.RequestHandler):
  def get(self,bid):
    if users.get_current_user() == None :
      self.redirect(users.create_login_url(self.request.uri))
      
    greeting = db.get(bid)
    if users.get_current_user() == greeting.author or users.is_current_user_admin():
      template_values = {
        'greeting': greeting,
      }
      path = os.path.join(os.path.dirname(__file__), 'template/editblog.html')
      self.response.out.write(template.render(path, template_values))
    else :
      self.redirect("/exception/hasnoright.html")

#Anybody who had writed the blog has the right to update it
class UpdateBlog(webapp.RequestHandler):
  def post(self):
    if users.get_current_user() == None :
      self.redirect(users.create_login_url(self.request.uri))
      
    greeting = db.get(self.request.get('key'))
    if users.get_current_user() == greeting.author or users.is_current_user_admin():
      greeting.title = self.request.get('title')
      greeting.tags = self.request.get('tags').split(' ')
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
    if users.get_current_user() == greeting.author or users.is_current_user_admin():
      greeting.delete()
      self.redirect('/')
    else :
      self.redirect("/exception/hasnoright.html")



      

application = webapp.WSGIApplication([
  ('/', MainPage),
  (r'/blog/(.*)', ViewBlog),
  ('/add', AddBlog),
  (r'/edit/(.*)', EditBlog),
  ('/update', UpdateBlog),
  (r'/delete/(.*)', DeleteBlog)  
], debug=True)


def main():
  logging.getLogger().setLevel(logging.INFO)
  wsgiref.handlers.CGIHandler().run(application)


DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
EXTRA_PATHS = [
  DIR_PATH,
  #os.path.join(DIR_PATH, 'utils'),
]
sys.path = EXTRA_PATHS + sys.path
logging.debug(sys.path)
from utils.textconvert import text2html
if __name__ == '__main__':
  main()
