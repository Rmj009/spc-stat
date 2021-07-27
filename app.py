# export DATABASE_URL='postgres://localhost:5432/
import time,os,redis
# ,html,sys,traceback
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
from utils.spcTable import SpcTable
from utils.gauge import Gauge
from errors import *
import pandas as pd
app = Flask(__name__, static_url_path='')
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


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


@app.route("/v1/capability-new", methods=['GET'])
def GormToCPR():
  points = request.args.get('points')
  usllst = request.args.get('USL') 
  lsllst = request.args.get('LSL')
  goodlst = request.args.get('good')
  defectlst = request.args.get('defect')
  measureAmount = request.args.get('measureAmount') #measureAmount
  stdValue = request.args.get('stdValue')
  try:
    if (points == None) or (len(points) == 0):
      result = 'PointsInvaild'
      return result, 400
    elif (usllst == None) or (len(usllst) == 0):
      result = 'USLInvaild'
      return result, 400
    elif (lsllst == None) or (len(lsllst) == 0):
      result = 'LSLInvaild'
      return result, 400
    elif (goodlst == None) or (len(goodlst) == 0):
      result = 'GOODInvaild'
      return result, 400
    elif (defectlst == None) or (len(defectlst) == 0):
      result = 'DefectInvaild'
      return result, 400
    elif (measureAmount == None) or (len(measureAmount) == 0):
      result = 'measureAmountInvaild'
      return result, 400
    elif (stdValue == None) or (len(stdValue) == 0):
      result = 'StdValueInvaild'
      return result, 400
    else:
      # GormResult = [points,[goodlst],[defectlst],[lsllst],[usllst],[measureAmount],[stdValue]]
      # CapabilityCol = ["points","goodlst","defectlst","lsllst","usllst","measureAmount","stdValue"]
      # GormResults = dict(zip(CapabilityCol, GormResult))
      result = Gauge.stats(points,goodlst,defectlst,lsllst,usllst,measureAmount,stdValue)
      return result, 200
  except Exception as errors:
    print('error',errors)
    return 'CalcFail',errors, 500



#-----------------ENTRANCE-----------------------
@app.route('/', methods=['GET'])
def home():
  # count = get_hit_count()
  # return ('API ok! Counting {} times.\n').format(count)
  return 'api ok!',200

if __name__ == "__main__":
  app.debug = True
  app.run(host=os.getenv('HOST'), debug=True, port=os.getenv('PORT'))
