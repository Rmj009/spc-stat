from logging import error
import sys,os #,redis
from os.path import abspath, dirname
from flask import request, render_template
from flask.json import jsonify
import requests, asyncio

"""
Internal import as below
"""
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from __init__ import *
from api.root import app2    # Blueprint example
from api.v1nelson import nelson
from api.v1capability import capability
from api.nelsonNew import GormToNelson
from api.capabilityNew import GormToCPR
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
  capability(app)
  nelson(app)

  with app.test_request_context():
    show_API_request(GormToNelson(app))
    show_API_request(GormToCPR(app))

# app.wsgi_app = printMiddleware(app.wsgi_app)
# status_code = printMiddleware(app.wsgi_app)

# 1. Get request header token: [SPC] request.header = xxx
# 2. Build user api (https://dotzerotech-user-api.dotzero.app/v2/permission/app?name=spc) request with auth token in header
# 3. ok: next
# not ok: abort()

# app.add_url_rule('', view_func=as_view('/v1/capability-new'))


async def async_check_auth(AuthorizationToken):
  url = os.getenv('DZ_TOKEN_PERMISSION')
  headers = { 'Authorization': AuthorizationToken}
  response = requests.request("GET", url, headers=headers) #, data=payload, files=files)
  # print('BUG2',response.status_code )
  json_text = response.json()
  # print('JSONTEXT::::::::;',json_text)
  if (response.status_code == 400):
    return render_template('400.html'), 400
  elif response.status_code != 200:
    return False
  elif json_text['access'] == True:
    return True
  else:
    return False

@app.before_request
def auth():
  # print('path: {0}, url: {1} , endpoint:{2}'.format(request.path, request.url,request.endpoint))
  try:
    header = request.headers
    endpoint = request.endpoint
    # print("///////////////////")
    # # print('show {0}{1}'.format(header,endpoint))
    # print("///////////////////")
  except AssertionError as asserr:
    raise asserr
  except Exception as eerr:
    print("///////////////////")
    print('show {0}'.format(eerr))
    print("///////////////////")

  if "Authorization" in header:
      AuthorizationToken =  header['Authorization']
      is_auth = asyncio.run(async_check_auth(AuthorizationToken))
      if is_auth != True:
        return render_template('401.html'), 401
      else:
        return 
  
  elif ("Authorization" not in header) and (endpoint == 'NelsonAPI' or endpoint == 'CPR'):
    # print("Nelson API or Capability API without BearerAuth", endpoint)
    return render_template('401.html'), 401
  
  elif ("Authorization" not in header) and ('app2' or 'static' in endpoint):
    print("requestendpoint",endpoint)
    # return render_template('401.html'), 401
    return

  else:
    print("NO AUTH header\n:::".format(request.url))
    return render_template('401.html'), 401
    # return

# loop = asyncio.get_event_loop()

# loop.run_until_complete(GormToNelson(app))

# loop2 = asyncio.get_event_loop()

# loop2.run_until_complete(GormToCPR(app))

#-----------------ENTRANCE-----------------------
if __name__ == "__main__":
  app.run(host=os.getenv('HOST'), debug=True, port=os.getenv('PORT') ) #,load_dotenv=True)

# flask run --host 0.0.0.0 --port 5000
