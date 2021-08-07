from utils.spcchart import SpcChart
from flask import request

def plotSPCchart(app):
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
