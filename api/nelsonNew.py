from flask import request,render_template
from fastapi import Depends
from utils.gauge import Gauge
# from ..auth.security import validate_request
# from ..models.nelsonNew import nelsonNew

import requests,os,asyncio
# from flask_api import status
# try:
#     print('path: {0}, url: {1} , endpoint:{2}'.format(request.path, request.url,request.endpoint))

# except Exception as ee:
#     print(ee)
# async def async_check_auth(AuthorizationToken):
#   url = os.getenv('DZ_TOKEN_PERMISSION')
#   headers = { 'Authorization': AuthorizationToken}
# #   # r = requests.get(url, headers=headers)
#   response = requests.request("GET", url, headers=headers) #, data=payload, files=files)
#   print('BUG2',response.status_code )
#   json_text = response.json()
#   print(json_text)
#   if (response.status_code == 400):
#     return render_template('400.html'), 400

#   elif response.status_code != 200:

#     return False
#     # 400, status.HTTP_400_BAD_REQUEST

#   elif json_text['access'] == True:

#     return True
#     # 400, status.HTTP_400_BAD_REQUEST

#   else:
#     return False

# def auth():

#   try:
#     header = request.headers
#     AuthorizationToken =  header['Authorization']
#   except Exception as eee:
#     return render_template('400.html'), 400
#   is_auth = asyncio.run(async_check_auth(AuthorizationToken))
  
#   if is_auth is not True:
#     return render_template('401.html'), 401



# auth()









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
                return result, 200

        except Exception as errors:
            print('SHOWerror',errors)
            return 'CalcFail', 500