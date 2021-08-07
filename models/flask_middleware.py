# from flask import Request
# from werkzeug.datastructures import Headers
from werkzeug.wrappers import Request
from flask.views import MethodView
import json,os
from flask import jsonify
from flask.views import MethodView
from itsdangerous import TimedJSONWebSignatureSerializer as TJSS



class printMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('— — — — — — — — — —')
        print('API called',self)
        print('— — — — — — — — — —')
        # not Flask request - from werkzeug.wrappers import Request
        request = Request(environ)
        # auth_token = request.environ.get('DZ_TOKEN_PERMISSION')
        print(f'Headerssss:',request.headers.get('Postman-Token'))
        # print(f'Headerssss:',request.headers) # coz api have no header initially
        # spcRequestHeader = request.headers.get(Headers)
        print('path: {0}, url: {1}'.format(request.path, request.url))
        # just do here everything what you need
        if request.headers is None :
            responses = jsonify(message = 'bad request')
            responses.status_code = 400
            return responses
        else:
            try:
                request.args.get(os.getenv('DZ_TOKEN_PERMISSION'),headers = request.headers)
                # print(str(flask_Request))
            except Exception as err:
                print(err)
            return self.app(environ, start_response)

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

class AuthorToken(MethodView):
    def post(self):
        # 產生token，有效期設置為3600秒
        s = TJSS( expires_in=3600)
        token = s.dumps({}).decode('utf-8')
        # 回傳符合RFC 6750的格式
        response = jsonify({
            'access_token': token,
            'token_type': 'Bearer',
            'expires_in': 3600
        })
        return response


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


