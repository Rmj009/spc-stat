from flask import request, abort
from fastapi import Depends
from utils.gauge import Gauge

def GormToNelson(app):
    @app.route("/v1/nelson-new", methods=['GET'])
    def NelsonAPI(
        # authentication: bool = Depends(validate_request)
    ):
        points = request.args.get('points')
        try:
            if (points == None) or (len(points) == 0):
                result = 'PointsInvaild'
                return result, 400
            else:
                result = Gauge.nelson(points)
                if ( result != None ):
                    return result, 200
                else:
                    return abort(400)

        except Exception as errors:
            print('SHOWerror',errors)
            return 'CalcFail', 500