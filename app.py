from logging import error
import sys,os #,redis
from os.path import abspath, dirname
from flask import Flask, request
from flask.json import jsonify
from werkzeug.datastructures import Headers
from werkzeug.wrappers import response
from flask.views import View
# import requests

# from flask_oauth import OAuth
# from flask_cors import CORS
# from flask_oauthlib.provider import OAuth2Provider
# https://pythonhosted.org/Flask-OAuth/

"""
import API as below
"""
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from .api.root import app2    # Blueprint example
from .api.docs import swaggerDOC
from .api.v1nelson import nelson
from .api.v1capability import capability
from .api.nelsonNew import GormToNelson
from .api.capabilityNew import GormToCPR
from .api.routes.errHandler import HandleFlaskerr
from .models.flask_middleware import printMiddleware


#######################################################
 #########  spc-backend-statistics START   ###########
#######################################################


app = Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.logger.debug('A value for debugging') #app.logger.error('An error occurred')
# cache = redis.Redis(host='redis', port=6379)

# class PassGateway:

# class BearerAuth_flask(object):
#   @app.before_request
#   def BearerAuth(token):
#     if token != None:
#       app.wsgi_app = printMiddleware(app.wsgi_app) # print API have called
#     else:
#       return token
#   # print('before request started')
#   # print('URL:{0}'.format(request.url))
#   # print('---------------')
#   # print(f'Headers:',request.headers)
#   # print('---------------')
  
  # print(type(request.headers))
  # print(str(request.headers))
  # print(request.form.get())
# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
  # if (routes != error) :{
# url = 'https://dotzerotech-user-api.dotzero.app/v2/permission/app?name=spc'

# headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImM1MzYyNGFmMTYwMGRhNzlmMzFmMDMxNGYyMDVkNGYzN2FkNmUyNDYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiRFogQWRtaW4iLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYWxlcnQtaGVpZ2h0LTI1NzMwNCIsImF1ZCI6ImFsZXJ0LWhlaWdodC0yNTczMDQiLCJhdXRoX3RpbWUiOjE2Mjc5ODI5ODIsInVzZXJfaWQiOiJiT2hlQlY2aDFQTjRTbG9wc2g0N1RneFZtWHYxIiwic3ViIjoiYk9oZUJWNmgxUE40U2xvcHNoNDdUZ3hWbVh2MSIsImlhdCI6MTYyNzk4Mjk4MiwiZXhwIjoxNjI3OTg2NTgyLCJlbWFpbCI6ImRldi5pb0Bkb3R6ZXJvLnRlY2giLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiZGV2LmlvQGRvdHplcm8udGVjaCJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIiwidGVuYW50IjoiZXh0ZW5kLWZvcm1pbmctaWlucW0ifX0.XgJS9gHCF7yT0EmS8yyOPRUfjZ9DafJYMJt6hqG6JaYXlMPL_BL-EsSYEHEGVjeV_C8M0bOcAyN19YCxJZ-011iFu-UOa8j_O6JKiodRS1FVgb53BZcu8yHw0IVF7KdM4ucpxL7f-KYp_Y7_0NbEfnltUcqWAFRkJFQjkiOPGHhQVy9ABUIJK7GJyftU4Y_G4Po386fteydVR0ouYzM1kRwXmEbElwyjrAhItfzjl4TnbeyX2xHeZPpsLlw1rUDhmo7iGIeSmq3e6o1V6B-kl7K6OpmQgHOf6CHntNFvNMD_vjmOq4OptKB01mDOa3hmg8TWDZ7RrQXbCvP7abjqmA'}
# r = requests.get(url, headers=headers)
# # https://docs.python-requests.org/en/master/

  # }
  # else:
    # abort request(400)
  


# 1. Get request header token: [SPC] request.header = xxx
# 2. Build user api (https://dotzerotech-user-api.dotzero.app/v2/permission/app?name=spc) request with auth token in header
# 3. ok: next
# not ok: abort()

# app.add_url_rule('', view_func=as_view('/v1/capability-new'))


class callAPI:
  app.wsgi_app = printMiddleware(app.wsgi_app)
  HandleFlaskerr(app)
  app.register_blueprint(app2)

  swaggerDOC(app)
  capability(app)
  nelson(app)
  GormToNelson(app)
  GormToCPR(app)


# @app.before_request
# def before_request2():
#     # print('before request started 2')
#     # print(request.url)
# https://dormousehole.readthedocs.io/en/latest/views.html
class ShowUsers(View):
  def dispatch_request(self):
    print(f'=========')
    # users = User.query.all()
    print(f'=========')
    return#, objects=users)


app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))

# oauth = OAuth()
# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)

@app.after_request
def after_request(response):
    print('after request finished')
    print(request.url)
    response.headers['key'] = 'value'
    # post_data = request.get_json()
    # print('PostData:',post_data)
    return response

# app.add_url_rule('/v1/capability-new', view_func=BearerAuth_flask.as_view('/v1/capability-new'))
# app.add_url_rule('/cap/', view_func=SPC_statistics.as_view('show_users'))



#-----------------ENTRANCE-----------------------
if __name__ == "__main__":
  app.debug = True
  app.run(host=os.getenv('HOST'), debug=True, port=os.getenv('PORT'))
