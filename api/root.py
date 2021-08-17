from flask import request, render_template, Blueprint, g

app2 = Blueprint('app2', __name__, static_folder='/static')

"""
Root.py API including:
1. root "/"
2. swagger docs
3. otherelse for rendering frontend
"""
@app2.route('/api-docs/')
# @exclude_from_analytics()
def get_docs():
    # print('Swagger:{0}',format(g.skip_analytics))
    return render_template('swaggerui.html')

@app2.route('/', methods=['GET'])
def home():
  g.name = "HOME"
#   count = get_hit_count()
  # return ('API ok! Counting {} times.\n').format(count)
  return '{0}'.format(g.name),200


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


############################################
############################################
############################################
"""
      frontend part:
      temporarily comment out until build up control chart project
"""
############################################
############################################
############################################
@app2.route('/app2')
def show():
  return "Hello Blueprint app2"


@app2.route('/front', methods=['GET','POST'])
def index():
  if request.method == "GET":
    try: 
      # return render_template('index2.html', title="spc_show", name = 'new_plot', url ='/static/Nelson65.png')
      return render_template('index2.html')
    except Exception as e:
      print('type of:\n',type(e),e)


#------------CONFIGURATION--------------
# print(os.getcwd()) # print the pwd status
#----------------GET-------------------
# @app.route('/front', methods=['GET','POST'])
# def index():
#   if request.method == "GET":
#     try: 
#       return render_template('index2.html', title="spc_show", name = 'new_plot', url ='/static/Nelson65.png')
#     except Exception as e:
#       print('type of:',type(e))

# @app.route('/plot.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='static/img/Nelson65.png')
# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig