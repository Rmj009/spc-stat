from flask import request
from fastapi import Depends
from ..utils.gauge import Gauge
from ..auth.security import validate_request
# from ..models.nelsonNew import nelsonNew

async def GormToNelson(app):
    @app.route("/v1/nelson-new", methods=['GET'])
    def NelsonAPI(
        authentication: bool = Depends(validate_request)
    ):
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