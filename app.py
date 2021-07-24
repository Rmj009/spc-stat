# export DATABASE_URL='postgres://localhost:5432/
import os
# ,html,sys,traceback
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
from utils.spcTable import SpcTable
from errors import *
app = Flask(__name__, static_url_path='')
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

#-----------------ENTRANCE-----------------------
@app.route('/', methods=['GET'])
def home():
  return 'API ok', 200

if __name__ == "__main__":
  app.debug = True
  app.run(host=os.getenv('HOST'), debug=True, port=os.getenv('PORT'))
