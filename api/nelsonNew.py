from flask import request, abort
from fastapi import Depends
from utils.gauge import Gauge

"""
Verify the input sequenes upon "Nelson Rules" via func::Nelsonfunc( 4 inputs shown as below)
4 inputs from user requests : (beginTime=begin, finalTime=endtime, wuuid=wuuid, suuid=suuid)
output: Nelson Array[rule1~rule8] that represent whether or not the sequenes obey the rules
For more detail pls refer to the utils.spcTable "Nelsonfunc"
"""



def GormToNelson(app):
    @app.route("/v1/nelson-new", methods=['GET'])
    def NelsonAPI(
        # authentication: bool = Depends(validate_request)
    ):
        points = request.args.get('points')
        LSL = request.args.get('LSL')
        USL = request.args.get('USL')
        
        try:
            if (points == None) or (len(points) == 0):
                result = 'PointsInvaild'
                return result, 400
            # elif (USL == None) or (len(USL) == 0):
            #     result = 'USLInvaild'
            #     return result, 400
            # elif (LSL == None) or (len(LSL) == 0):
            #     result = 'LSLInvaild'
            #     return result, 400  

            else:
                result = Gauge.nelson(points, LSL, USL)
                if ( result != None ):
                    return result, 200
                else:
                    return abort(400)

        except Exception as errors:
            print('SHOWerror',errors)
            return 'CalcFail', 500