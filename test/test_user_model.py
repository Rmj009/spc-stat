import unittest
# from ..app.server import db
# from app.server.models import User
# from ..app.tests.base import BaseTestCase

from ..app import *

from flask import request


def generate_report():
    # format = request.args.get('format')
    print('path: {0}, url: {1} , endpoint:{2}'.format(request.path, request.url,request.endpoint))

with app.test_request_context():
    generate_report()

# class TestUserModel(BaseTestCase):

#     def test_encode_auth_token(self):
#         user = User(
#             email='test@test.com',
#             password='test'
#         )
#         db.session.add(user)
#         db.session.commit()
#         auth_token = user.encode_auth_token(user.id)
#         self.assertTrue(isinstance(auth_token, bytes))

if __name__ == '__main__':
    unittest.main()