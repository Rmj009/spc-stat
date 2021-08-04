from flask_sqlalchemy import SQLAlchemy
from flask import render_template
# import request
# from flask import request
# from app import app
db = SQLAlchemy()

#-------ERROR Handling----------
"""
500 bad request for exception
Returns:
500 and msg which caused problems
"""
# @app.route('/oauth/authorize', methods=['GET', 'POST'])
# @require_login
# @oauth.authorize_handler
# def authorize(*args, **kwargs):
#     if request.method == 'GET':
#         client_id = kwargs.get('client_id')
#         client = Client.query.filter_by(client_id=client_id).first()
#         kwargs['client'] = client
#         return render_template('oauthorize.html', **kwargs)

#     confirm = request.form.get('confirm', 'no')
#     return confirm == 'yes'


# class PassGateway:
# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('404.html'),error, 404

# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('500.html'),error, 500

# @app.teardown_appcontext
# def shotdown_session(error):
#     print ("@app.teardown_appcontext: shotdown_session()")
#     db.session.remove()
#     db.session.rollback()
#     return error, 500
