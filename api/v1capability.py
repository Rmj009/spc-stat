# from ..utils.spcTable import SpcTable
# from flask import request

# def capability(app):
#     @app.route("/v1/capability", methods=['GET'])
#     def v1capability(): # query params
#         begin = request.args.get('startTime')
#         endtime = request.args.get('endTime') 
#         wuuid = request.args.get('workOrderOpHistoryUUID')
#         suuid = request.args.get('spcMeasurePointConfigUUID')  
#         try:
#             if (begin == None) or (len(begin) == 0):
#                 result = 'startTimeError'
#                 return result, 400
#             elif (endtime == None) or (len(endtime) == 0):
#                 result = 'endTimeError'
#                 return result, 400
#             elif (suuid == None) or (len(suuid) == 0):
#                 result = 'configPointErr'
#                 return result, 400
#             else:
#                 result = SpcTable.CPRfunc(beginTime=begin, finalTime=endtime, wuuid=wuuid, suuid=suuid)
#                 return result, 200
#         except Exception as errors:
#             return ' Failure %s:',errors, 500