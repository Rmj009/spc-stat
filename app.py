from logging import error
import sys,os #,redis
from os.path import abspath, dirname
from flask import Flask ,request, abort, render_template ,Blueprint,redirect
from flask.json import jsonify

# from werkzeug.datastructures import Headers
# from werkzeug.wrappers import response
from flask.views import View
import requests, asyncio



# from flask_oauth import OAuth
# from flask_cors import CORS
# from flask_oauthlib.provider import OAuth2Provider
# https://pythonhosted.org/Flask-OAuth/

"""
import API as below
"""
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from .__init__ import *
from .api.root import app2    # Blueprint example
# from .api.v1nelson import nelson
# from .api.v1capability import capability
from .api.nelsonNew import GormToNelson
from .api.capabilityNew import GormToCPR
from .api.routes.flask_middleware import printMiddleware

#######################################################
 #########  spc-backend-statistics START   ###########
#######################################################

app.register_blueprint(app2)


# app.wsgi_app = printMiddleware(app.wsgi_app)
# status_code = printMiddleware(app.wsgi_app)
# print(status_code)
# def flaskerrs():
#   status_code = printMiddleware(app.wsgi_app)
#   @app.errorhandler(404)
#   def page_not_found(error):
#     return render_template('page_not_found.html'), 404
#   if (status_code ==  400):
#       # print( json.loads(response.text)['message']) #message offer by dotzero API
#       # print('render_template('400.html)')
#       # return response.status_code
#       # abort(400)
#       return render_template('400.html')
#       # return 400, status.HTTP_400_BAD_REQUEST

#   elif (status_code ==  401):
#       # print(json.loads(response.text)['message']) #message offer by dotzero API
#       # print('render_template('401.html)')
#       return render_template('400.html')
#       # return 400, status.HTTP_400_BAD_REQUEST
#       # return abort(401)

#   elif (status_code ==  500):
#       print(json.loads(response.text)['message']) #message offer by dotzero API
#       # print('render_template('500.html)')
#       return '400'
# class BearerAuth_flask(object):

  # if token != None:
  #   app.wsgi_app = printMiddleware(app.wsgi_app) # print API have called
  # else:
  #   return token
  # # print('before request started')
#   # print('URL:{0}'.format(request.url))
#   # print('---------------')
#   # print(f'Headers:',request.headers)
#   # print('---------------')
  
#   print(type(request.headers))
#   print(str(request.headers))
#   print(request.form.get())
# # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
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



import requests
# from flask_api import status

async def async_check_auth(AuthorizationToken):
  url = os.getenv('DZ_TOKEN_PERMISSION')
  headers = { 'Authorization': AuthorizationToken}
#   # r = requests.get(url, headers=headers)
  response = requests.request("GET", url, headers=headers) #, data=payload, files=files)
  print('BUG2',response.status_code )
  json_text = response.json()
  print(json_text)
  if (response.status_code == 400):
    return render_template('400.html'), 400

  elif response.status_code != 200:

    return False
    # 400, status.HTTP_400_BAD_REQUEST

  elif json_text['access'] == True:

    return True
    # 400, status.HTTP_400_BAD_REQUEST

  else:
    return False

@app.before_request
def auth():
  # run_analytics = True
  # if request.endpoint in app.view_functions:
  #       view_func = app.view_functions[request.endpoint]
  #       run_analytics = not hasattr(view_func, '_exclude_from_analytics')
  # print(request.path, run_analytics)
  
  # print('mmmm\n',header)
  # if 'logged_in' not in session and request.endpoint != 'login':
  #   return redirect(url_for('login'))
  try:
    header = request.headers
    AuthorizationToken =  header['Authorization']
  except Exception as eee:
    return render_template('400.html'), 400
  is_auth = asyncio.run(async_check_auth(AuthorizationToken))
  
  if is_auth is not True:
    return render_template('401.html'), 401
  

# @app.errorhandler(404)
# def page_not_found(error):
#   return render_template('404.html'), 404

# def mock_request(app):

#   @app.before_request
#   def BearerAuth(app):
#     app.wsgi_app = printMiddleware(app.wsgi_app)

#     return

class callAPI:
  # capability(app)
  # nelson(app)
  GormToNelson(app)
  GormToCPR(app)
# flask request
# print('path: {0}, url: {1} , endpoint:{2}'.format(request.path, request.url,request.endpoint))

# loop = asyncio.get_event_loop()

# loop.run_until_complete(GormToNelson(app))

# loop2 = asyncio.get_event_loop()

# loop2.run_until_complete(GormToCPR(app))


# @app.before_request
# def before_request2():
#     # print('before request started 2')
#     # print(request.url)
# https://dormousehole.readthedocs.io/en/latest/views.html
# class ShowUsers(View):
#   def dispatch_request(self):
#     print(f'=========')
#     # users = User.query.all()
#     print(f'=========')
#     return#, objects=users)



# app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))

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

# @app.after_request
# # def after_request(response):
#     # print('after request finished')
#     # print(request.url)
#     # response.headers['key'] = 'value'
#     # post_data = request.get_json()
#     # print('PostData:',post_data)
#     print(response)
#     # return response

# app.add_url_rule('/v1/capability-new', view_func=BearerAuth_flask.as_view('/v1/capability-new'))
# app.add_url_rule('/cap/', view_func=SPC_statistics.as_view('show_users'))


# app.wsgi_app = printMiddleware(app.wsgi_app)
#-----------------ENTRANCE-----------------------
if __name__ == "__main__":
  app.run(host=os.getenv('HOST'), debug=True, port=os.getenv('PORT'))
