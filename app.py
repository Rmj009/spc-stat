from logging import error
import time,os #,redis
# ,html,sys,traceback
from flask import Flask, request, render_template, g
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import Headers
from werkzeug.wrappers import response
from flask.views import View
import requests

# from flask_oauth import OAuth
# from flask_oauthlib.provider import OAuth2Provider
# https://pythonhosted.org/Flask-OAuth/

# from flask_cors import CORS
from components.flask_middleware import printMiddleware
from utils.spcTable import SpcTable
from utils.gauge import Gauge
from utils.spcchart import SpcChart
from api.nelsonNew import GormToNelson
from api.capabilityNew import GormToCPR

app = Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.logger.debug('A value for debugging')
app.logger.error('An error occurred')
# cache = redis.Redis(host='redis', port=6379)
# auth_flask.
db = SQLAlchemy()
# class PassGateway:
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),error, 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'),error, 500

# @app.teardown_appcontext
# def shotdown_session(error):
#     print ("@app.teardown_appcontext: shotdown_session()")
#     db.session.remove()
#     db.session.rollback()
#     return error, 500


# class BearerAuth_flask(object):

# @app.before_request
# def BearerAuth(token):
#   if token != None:
#     app.wsgi_app = printMiddleware(app.wsgi_app) # print API have called
#   # print('before request started')
#   # print('URL:{0}'.format(request.url))
#   # print('---------------')
#   # print(f'Headers:',request.headers)
#   # print('---------------')
#   g.name = "Authorization"
  
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


# @app.before_request
# def before_request2():
#     # print('before request started 2')
#     # print(request.url)
class ShowUsers(View):
# https://dormousehole.readthedocs.io/en/latest/views.html
    def dispatch_request(self):
      print(f'=========')
        # users = User.query.all()
      return render_template('index2.html')#, objects=users)

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


#------------CONFIGURATION--------------
# print(os.getcwd()) # print the pwd status
#----------------GET-------------------
# @app.route('/plot.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='static/img/Nelson65.png')
# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig

@app.route('/front', methods=['GET','POST'])
def index():
  if request.method == "GET":
    try: 
      return render_template('index2.html', title="spc_show", name = 'new_plot', url ='/static/Nelson65.png')
    except Exception as e:
      print('type of:',type(e))

@app.route('/api-docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')

@app.route("/v1/capability", methods=['GET'])
def capability():
  # query params
  try:
    begin = request.args.get('startTime')
    endtime = request.args.get('endTime') 
    wuuid = request.args.get('workOrderOpHistoryUUID')
    suuid = request.args.get('spcMeasurePointConfigUUID')  
    
    if (begin == None) or (len(begin) == 0):
      result = 'startTimeError'
      return result, 400
    elif (endtime == None) or (len(endtime) == 0):
      result = 'endTimeError'
      return result, 400
    elif (suuid == None) or (len(suuid) == 0):
      result = 'configPointErr'
      return result, 400
    else:
      result = SpcTable.CPRfunc(beginTime=begin, finalTime=endtime, wuuid=wuuid, suuid=suuid)
      return result, 200
  except Exception as errors:
    return ' Failure %s:',errors, 500

@app.route("/v1/nelson", methods=['GET'])
def nelson():
  begin = request.args.get('startTime')
  endtime = request.args.get('endTime') 
  wuuid = request.args.get('workOrderOpHistoryUUID')
  suuid = request.args.get('spcMeasurePointConfigUUID')
  try:
    if (suuid == None) or (len(suuid) == 0):
      result = 'config point error'
      return result, 400
    elif (begin == None) or (len(begin) == 0):
      result = 'start time error'
      return result, 400
    elif (endtime == None) or (len(endtime) == 0):
      result = 'end time error'
      return result, 400
    else:
      result = SpcTable.Nelsonfunc(beginTime=begin, finalTime=endtime, wuuid=wuuid, suuid=suuid)
      return result, 200
  except Exception as errors:

    print('error',errors)
    return 'Query Fail',errors, 500


class SPC_statistics(object):

  @app.route("/v1/spchart", methods=['GET'])
  def spcChart():
    points = request.args.get('points')
    try:
      if (points == None) or (len(points) == 0):
        result = 'PointsInvaild'
        return result, 400
      else:
        # result = Gauge.nelson(points)
        result = SpcChart(data = points)
        return result, 200

    except Exception as errors:
      print('SHOWerror',errors)
      return 'CalcFail', 500


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


GormToNelson(app)
GormToCPR(app)
#-----------------ENTRANCE-----------------------
@app.route('/', methods=['GET'])
def home():
  # count = get_hit_count()
  # return ('API ok! Counting {} times.\n').format(count)
  return '{0}'.format(g.name),200

# @app.teardown_request
# def teardown_request(Exception):
#   print ('teardown request')
#   print (request.url)
#   # raise Exception


if __name__ == "__main__":
  app.debug = True
  app.run(host=os.getenv('HOST'), debug=True, port=os.getenv('PORT'))
