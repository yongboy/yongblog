import os
from google.appengine.ext.webapp import template

import cgi
import datetime
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.ext import webapp

import pojo

class TagBlog(webapp.RequestHandler):
  def get(self,tag):
    
    greetings = db.GqlQuery("SELECT * "
                            "FROM Greeting "
                            "WHERE tags = :1 "
                            "ORDER BY date DESC",tag)
    template_values = {
      'tag': tag,
      'greetings': greetings
    }

    path = os.path.join(os.path.dirname(__file__), 'tagbloglist.html')
    self.response.out.write(template.render(path, template_values))
      

application = webapp.WSGIApplication([
  (r'/tags/(.*)', TagBlog)
], debug=True)


def main():
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
