from flask import render_template
from flask import request

@app.route('/front', methods=['GET','POST'])
def index():
  if request.method == "GET":
    try: 
      return render_template('index2.html', title="spc_show", name = 'new_plot', url ='/static/Nelson65.png')
    except Exception as e:
      print('type of:',type(e))