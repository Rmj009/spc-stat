# from app import app
from flask import request
from ..utils.gauge import Gauge

def GormToNelson(app):
    @app.route("/v1/nelson-new", methods=['GET'])
    def NelsonAPI():
        points = request.args.get('points')
        try:
            if (points == None) or (len(points) == 0):
                result = 'PointsInvaild'
                return result, 400
            else:
                result = Gauge.nelson(points)
                return result, 200

        except Exception as errors:
            print('SHOWerror',errors)
            return 'CalcFail', 500