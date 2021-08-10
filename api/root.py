from flask import render_template, Blueprint, g

app2 = Blueprint('app2', __name__, static_folder='/static')

### maybe call many api just in a .py
@app2.route('/api-docs/')
def get_docs():
    print('SHOW SWAGGER')
    return render_template('swaggerui.html')

@app2.route('/', methods=['GET'])
def home():
  g.name = "Authorization"
#   count = get_hit_count()
  # return ('API ok! Counting {} times.\n').format(count)
  return '{0}'.format(g.name),200


# def before_my_blueprint():
#     print(111)


@app2.route('/app2')
def show():
  return "Hello Blueprint app2"


