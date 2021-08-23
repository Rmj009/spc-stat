from utils.spcchart import SpcChart
from flask import request, abort

"""
spchart.py API including:
1. Plot the control chart for univariate 
"""

def plotSPCchart(app):
  @app.route("/v1/spchart", methods=['GET'])
  def spcChart():
    points = request.args.get('points')
    points = [ float(i) for i in points.split(',')]
    try:
      if (points == None) or (len(points) == 0):
        result = 'PointsInvaild'
        return result, 400
      else:
        # result = Gauge.nelson(points)
        result = SpcChart(data = points)
        if ( result != None ):
          return result, 200
        else:
          return abort(400)

    except Exception as errors:
      print('SHOWerror',errors)
      return 'CalcFail', 500
