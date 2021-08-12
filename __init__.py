from __future__ import absolute_import
from flask import Flask
# from .api.routes import errHandler
from api.routes import errHandler
app = Flask(__name__, static_url_path='/static', static_folder = "static") #static_folder=''
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.logger.debug('Debugging') #app.logger.error('An error occurred')
errHandler.HandleFlaskerr(app)

