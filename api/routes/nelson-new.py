


#   @app.route("/v1/nelson-new", methods=['GET'])
#   def GormToNelson():
#     points = request.args.get('points')
#     try:
#       if (points == None) or (len(points) == 0):
#         result = 'PointsInvaild'
#         return result, 400
#       else:
#         result = Gauge.nelson(points)
#         return result, 200

#     except Exception as errors:
#       print('SHOWerror',errors)
#       return 'CalcFail', 500