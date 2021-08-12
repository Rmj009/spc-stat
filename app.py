from logging import error
import re
import sys,os #,redis
from os.path import abspath, dirname
from flask import url_for, session,request, abort, render_template ,redirect, g
from flask.json import jsonify
# from werkzeug.datastructures import Headers
# from werkzeug.wrappers import response
from flask.views import View
import requests, asyncio
# from flask_api import status
# from flask_oauth import OAuth
# from flask_cors import CORS
# from flask_oauthlib.provider import OAuth2Provider
# https://pythonhosted.org/Flask-OAuth/

"""
Internal import as below
"""
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from .__init__ import *
# from __init__ import *
from .api.root import app2, show    # Blueprint example
# from api.root import app2, show    # Blueprint example
# from .api.v1nelson import nelson
# from .api.v1capability import capability
from .api.nelsonNew import GormToNelson
from .api.capabilityNew import GormToCPR
# from api.nelsonNew import GormToNelson
# from api.capabilityNew import GormToCPR
# from api.routes.flask_middleware import printMiddleware

#######################################################
 #########  spc-backend-statistics START   ###########
#######################################################


app.register_blueprint(app2)
def show_API_request(object):
    # format = request.args.get('format')
    print('path: {0}, url: {1} , endpoint:{2}'.format(request.path, request.url,request.endpoint))
    return

class callAPI:
  # capability(app)
  # nelson(app)

  with app.test_request_context():
    GormToNelson(app)
    
    show_API_request(GormToCPR(app))

# app.wsgi_app = printMiddleware(app.wsgi_app)
# status_code = printMiddleware(app.wsgi_app)

# 1. Get request header token: [SPC] request.header = xxx
# 2. Build user api (https://dotzerotech-user-api.dotzero.app/v2/permission/app?name=spc) request with auth token in header
# 3. ok: next
# not ok: abort()

# app.add_url_rule('', view_func=as_view('/v1/capability-new'))

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Token is missing.'}, 401

        if token != 'mytoken':
            return {'message' : 'Your token is wrong, wrong, wrong!!!'}, 401

        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated


async def async_check_auth(AuthorizationToken):
  url = os.getenv('DZ_TOKEN_PERMISSION')
  headers = { 'Authorization': AuthorizationToken}
#   # r = requests.get(url, headers=headers)
  response = requests.request("GET", url, headers=headers) #, data=payload, files=files)
  print('BUG2',response.status_code )
  json_text = response.json()
  print('JSONTEXT::::::::;',json_text)
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
  
  print(session.get(key='nelson-new'))
  print('path: {0}, url: {1} , endpoint:{2}'.format(request.path, request.url,request.endpoint))
  header = request.headers
  endpoint = request.endpoint
  print("///////////////////")
  print('show',header,endpoint)
  print("///////////////////")
  if "Authorization" in header: 
      print("header auth yes")
      AuthorizationToken =  header['Authorization']
      is_auth = asyncio.run(async_check_auth(AuthorizationToken))
      if is_auth != True:
        return render_template('401.html'), 401
      else:
          # app.register_blueprint(app2)
        return 
  
  elif ("Authorization" not in header) and ('NelsonAPI'== endpoint or 'CPR'== endpoint):
    print("requestendpoint",endpoint)
    print("Nelson API or Capability API without BearerAuth", request.endpoint)
    return render_template('401.html'), 401
  
  
  elif ("Authorization" not in header) and ('app2' or 'static' in endpoint):
    print("requestendpoint",endpoint)
    # print("Nelson API or Capability API without BearerAuth", request.endpoint)
    # return render_template('401.html'), 401
    return

  else:
    print("NO AUTH header\n")
    print(" request.url ",  request.url )
    return render_template('401.html'), 401
    # return


  # try:
  #   print("try: lol...")
  #   # check header auth is exist or not 
  #   #  1. x ----> endpoint (auth required) API ----> GGG 
  #   #  2. x ----> endpoint (auth free) ----> 
  #   AuthorizationToken =  header['Authorization']
  # except AssertionError:
  #   # app.register_blueprint(app2)
  #   return
  # except Exception as eee:
  #   print("[Exception] lol...", eee)
  #   return render_template('400.html'), 400
  # print("endpoint[outside]: ", request)

  # if request.endpoint == 'NelsonAPI' or 'CPR':
  #   print("endpoint [yuting]: ", request)
  #   is_auth = asyncio.run(async_check_auth(AuthorizationToken))
  #   if is_auth != True:
  #     return render_template('401.html'), 401

  #   else:
  #     # app.register_blueprint(app2)
  #     return 

  # else:
  #   print("FreeAuth")
  #   return


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



#-----------------ENTRANCE-----------------------
if __name__ == "__main__":
  app.run(host=os.getenv('HOST'), debug=True, port=os.getenv('PORT'),load_dotenv=True)



# flask run --host 0.0.0.0 --port 5000
