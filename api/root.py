from flask import Blueprint

app2 = Blueprint('app2', __name__, static_folder='/static')

### maybe call many api just in a .py

@app2.route('/app2')
def show():
        return "Hello Blueprint app2"