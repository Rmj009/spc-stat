# from flask import request, abort
# from utils.nelsonrule4 import 

# """
# Verify the specification out of boundary or not
# """

# def check_lsl_usl(app):
#     @app.route("/v1/check-lslusl", methods=['GET'])
#     def spectestAPI(
#         # authentication: bool = Depends(validate_request)
#     ):
#         points = request.args.get('points')
#         LSL = request.args.get('LSL')
#         USL = request.args.get('USL')
        
#         try:
#             if (points == None) or (len(points) == 0):
#                 result = 'PointsInvaild'
#                 return result, 400
#             elif (USL == None) or (len(USL) == 0):
#                 result = 'USLInvaild'
#                 return result, 400
#             elif (LSL == None) or (len(LSL) == 0):
#                 result = 'LSLInvaild'
#                 return result, 400        
#             else:
#                 result = (points)
#                 if ( result != None ):
#                     return result, 200
#                 else:
#                     return abort(400)

#         except Exception as errors:
#             print('SHOWerror',errors)
#             return 'CalcFail', 500