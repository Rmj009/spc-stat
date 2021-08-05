# from flask import Request
from werkzeug.wrappers import Request
import json


class printMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('— — — — — — — — — —')
        print('API called')
        print('— — — — — — — — — —')
        # not Flask request - from werkzeug.wrappers import Request
        request = Request(environ)
        # print(f'Headerssss:',request.headers.get('Postman-Token'))
        print(f'Headerssss:',request.headers.get('Postman-Token'))
        print('path: {0}, url: {1}'.format(request.path, request.url))
        # just do here everything what you need

        return self.app(environ, start_response)


def test_valid_blacklisted_token_logout(self):
    """ Test for logout after a valid token gets blacklisted """
    with self.client:
        # user registration
        resp_register = self.client.post(
            '/auth/register',
            # data=json.dumps(dict(
            #     email='joe@gmail.com',
            #     password='123456'
            # )),
            content_type='application/json',
        )
        # data_register = json.loads(resp_register.data.decode())
        self.assertTrue(data_register['status'] == 'success')
        self.assertTrue(
            data_register['message'] == 'Successfully registered.')
        self.assertTrue(data_register['auth_token'])
        self.assertTrue(resp_register.content_type == 'application/json')
        self.assertEqual(resp_register.status_code, 201)
        # user login
        resp_login = self.client.post(
            '/auth/login',
            data=json.dumps(dict(
                email='joe@gmail.com',
                password='123456'
            )),
            content_type='application/json'
        )
        data_login = json.loads(resp_login.data.decode())
        self.assertTrue(data_login['status'] == 'success')
        self.assertTrue(data_login['message'] == 'Successfully logged in.')
        self.assertTrue(data_login['auth_token'])
        self.assertTrue(resp_login.content_type == 'application/json')
        self.assertEqual(resp_login.status_code, 200)
        # blacklist a valid token
        # blacklist_token = BlacklistToken(token=json.loads(resp_login.data.decode())['auth_token'])
        # db.session.add(blacklist_token)
        # db.session.commit()
        # blacklisted valid token logout
        response = self.client.post(
            '/auth/logout',
            headers=dict(
                Authorization='Bearer ' + json.loads(
                    resp_login.data.decode()
                )['auth_token']
            )
        )
        data = json.loads(response.data.decode())
        self.assertTrue(data['status'] == 'fail')
        self.assertTrue(data['message'] == 'Token blacklisted. Please log in again.')
        self.assertEqual(response.status_code, 401)