# from flask import Request
# from werkzeug.datastructures import Headers
from werkzeug.wrappers import Request
# from flask.views import MethodView
import json,os
from flask import app, jsonify, abort, render_template
from flask.views import MethodView
# from itsdangerous import TimedJSONWebSignatureSerializer as TJSS
import requests
from flask_api import status
from api.routes import errHandler
errHandler.HandleFlaskerr(app)


class printMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('— — — — — — — — — —')
        print('API called',self.app)
        print('— — — — — — — — — —')
        request = Request(environ) # not Flask request - from werkzeug.wrappers import Request
        payload={}
        files={}
        try:
            url = os.getenv('DZ_TOKEN_PERMISSION') #request.environ.get
            headers = {'Authorization': request.headers.get('Authorization')} # coz api have no header initially
            # print(headers)
            # print('path: {0}, url: {1} , endpoint:{2}'.format(request.path, request.url,request.endpoint))
            response = requests.request("GET", url, headers=headers, data=payload, files=files)
            print('BUGG',response.text)
            print('BUG2',response.status_code )
            if (response.status_code ==  400):
                print( json.loads(response.text)['message']) #message offer by dotzero API
                # print('render_template('400.html)')
                # return response.status_code
                # return str(response.text),400
                # return 400, status.HTTP_400_BAD_REQUEST
                return render_template('400.html')

            elif (response.status_code ==  401):
                print(json.loads(response.text)['message']) #message offer by dotzero API
                # print('render_template('401.html)')
                return response.status_code
                # return 400, status.HTTP_400_BAD_REQUEST
                # return abort(401)

            elif (response.status_code ==  500):
                print(json.loads(response.text)['message']) #message offer by dotzero API
                # print('render_template('500.html)')
                return '400'
                # return 400, status.HTTP_400_BAD_REQUEST
                # return abort(500)
        
            else:
                # print()
                # return response.status_code
                return self.app(environ, start_response)
        
        except Exception as error:
                print('MiddleWare Fault:',error)
                # abort(400)
                # return 500, status.HTTP_500_INTERNAL_SERVER_ERROR

    

        

            

        # if (response.status_code !=  200):
        #     pass
        # # (json.loads(response.text)['access'] != True):
        #     # print('kevinss',json.loads(response.text)['access'])
        #     return

        
        
        # else:
        #     if (json.loads(response.text)['message'] not in 'missing key in request header') or (json.loads(response.text)['access'] != True):
        #         print('kevinss',json.loads(response.text)['access'])
        #         return abort(400)
        #     # return 400, status.HTTP_400_BAD_REQUEST

        #     elif (json.loads(response.text)['message'] not in 'Unauthorized') or (json.loads(response.text)['access'] != True):
        #         print('unauthorized value')
        #         return abort(401)
        #     # return 401, status.HTTP_401_UNAUTHORIZED
           
        # if request.headers is None :
        #     responses = jsonify(message = 'bad request')
        #     responses.status_code = 400
        #     return responses
        
        # else:
        #     try:
        #         pass
        #         # print('kevinResponse`',response)
        #         # print('path: {0}, url: {1}'.format(request.path, url))
        #         # ans = response['access']
        #         # print('ans,', ans)
        #         # request.args.get(os.getenv('DZ_TOKEN_PERMISSION'),headers = request.headers)
        #         # print(str(flask_Request))
        #         return
            
        
    # def get(self):
    #     # 首先驗證token的確認性與效期，為了版面的簡潔並沒有做try，但實務上會建議做一下try except
    #     token_type, access_token = request.headers.get('Authorization').split(' ')
    #     if token_type != 'Bearer' or token_type is None:
    #         # 驗證token_type是否為Bearer
    #         pass

    #     s = TJSS(app.config['SECRET_KEY'])
    #     data = s.loads(access_token)
    #     return jsonify({'data': data['username']})

# app.config['SECRET_KEY'] = 'ABCDEFhijklm'

# class AuthorToken(MethodView):
#     def post(self):
#         # 產生token，有效期設置為3600秒
#         s = TJSS( expires_in=3600)
#         token = s.dumps({}).decode('utf-8')
#         # 回傳符合RFC 6750的格式
#         response = jsonify({
#             'access_token': token,
#             'token_type': 'Bearer',
#             'expires_in': 3600
#         })
#         return response


# class FakeSource(MethodView):
#     def get(self):
#         # 首先驗證token的確認性與效期，為了版面的簡潔並沒有做try，但實務上會建議做一下try except
#         token_type, access_token = request.headers.get('Authorization').split(' ')
#         if token_type != 'Bearer' or token_type is None:
#             # 驗證token_type是否為Bearer
#             pass

#         s = TJSS(app.config['SECRET_KEY'])
#         data = s.loads(access_token)
#         return jsonify({'data': data['username']})

# def test_valid_blacklisted_token_logout(self):

#     """ Test for logout after a valid token gets blacklisted """
#     with self.client:
#         # user registration
#         resp_register = self.client.post(
#             '/auth/register',
#             # data=json.dumps(dict(
#             #     email='joe@gmail.com',
#             #     password='123456'
#             # )),
#             content_type='application/json',
#         )
#         # data_register = json.loads(resp_register.data.decode())
#         self.assertTrue(data_register['status'] == 'success')
#         self.assertTrue(
#             data_register['message'] == 'Successfully registered.')
#         self.assertTrue(data_register['auth_token'])
#         self.assertTrue(resp_register.content_type == 'application/json')
#         self.assertEqual(resp_register.status_code, 201)
#         # user login
#         resp_login = self.client.post(
#             '/auth/login',
#             data=json.dumps(dict(
#                 email='joe@gmail.com',
#                 password='123456'
#             )),
#             content_type='application/json'
#         )
#         data_login = json.loads(resp_login.data.decode())
#         self.assertTrue(data_login['status'] == 'success')
#         self.assertTrue(data_login['message'] == 'Successfully logged in.')
#         self.assertTrue(data_login['auth_token'])
#         self.assertTrue(resp_login.content_type == 'application/json')
#         self.assertEqual(resp_login.status_code, 200)
#         # blacklist a valid token
#         # blacklist_token = BlacklistToken(token=json.loads(resp_login.data.decode())['auth_token'])
#         # db.session.add(blacklist_token)
#         # db.session.commit()
#         # blacklisted valid token logout
#         response = self.client.post(
#             '/auth/logout',
#             headers=dict(
#                 Authorization='Bearer ' + json.loads(
#                     resp_login.data.decode()
#                 )['auth_token']
#             )
#         )
#         data = json.loads(response.data.decode())
#         self.assertTrue(data['status'] == 'fail')
#         self.assertTrue(data['message'] == 'Token blacklisted. Please log in again.')
#         self.assertEqual(response.status_code, 401)

