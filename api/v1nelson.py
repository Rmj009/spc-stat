from utils.spcTable import SpcTable
from flask import request, abort


"""
Verify the input sequenes upon "Nelson Rules" via func::Nelsonfunc( 4 inputs shown as below) through DB
4 inputs from user requests : (beginTime=begin, finalTime=endtime, wuuid=wuuid, suuid=suuid)
output: Nelson Array[rule1~rule8] that represent whether or not the sequenes obey the rules
For more detail pls refer to the utils.spcTable "Nelsonfunc"
"""


def nelson(app):
    @app.route("/v1/nelson", methods=['GET'])
    def v1nelson():
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
                if ( result != None ):
                    return result, 200
                else:
                    return abort(400)
        except Exception as errors:
            print('error',errors)
            return 'Query Fail',errors, 500