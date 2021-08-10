from flask import render_template, make_response
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

def HandleFlaskerr(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'),error, 404

    @app.errorhandler(500)
    def internal_error(error):
        # db.session.rollback() #coz python wont sync with postgres
        return render_template('500.html'),error, 500

    @app.errorhandler(400)
    def page_not_found(error):
        return render_template('400.html'), 400

    @app.errorhandler(400)
    def not_found(error):
        resp = make_response(render_template('400.html'), 400)
        resp.headers['X-Something'] = 'A value'
        return resp

