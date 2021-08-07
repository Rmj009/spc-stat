from flask import render_template

def swaggerDOC(app):
    @app.route('/api-docs/')
    def get_docs():
        print('sending docs')
        return render_template('swaggerui.html')
