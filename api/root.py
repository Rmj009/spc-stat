from flask import render_template, Blueprint, g

app2 = Blueprint('app2', __name__, static_folder='/static')

### maybe call many api just in a .py

# def exclude_from_analytics(*args, **kw):
#     def wrapper(endpoint_method):
#         endpoint_method._skip_analytics = True

#         @wraps(endpoint_method)
#         def wrapped(*endpoint_args, **endpoint_kw):
#             # This is what I want I want to do. Will not work.
#             # g.skip_analytics = getattr(endpoint_method, '_skip_analytics', False)
#             return endpoint_method(*endpoint_args, **endpoint_kw)
#         return wrapped
#     return wrapper

@app2.route('/api-docs/')
# @exclude_from_analytics()
def get_docs():
    # print('Swagger:{0}',format(g.skip_analytics))
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


