from flask import render_template
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

