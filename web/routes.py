"""Route declaration."""
from flask import current_app as app
from flask import render_template

from web.control.latex import all_equations, equation_by_name, all_equation_names

@app.route('/')
def home():
    """Landing page."""
    nav = [{'name': 'Дом', 'url': '#'},
           {'name': 'Latex', 'url': '/latex/'}]
    return render_template('home.html',
                           nav=nav,
                           title="WebEquations",
                           description="Description")

@app.route('/latex/')
def latex():
    # load('S')
    # with open('/home/alice/Documents/Course/tatarinov_equation/web/tmp.txt', 'r') as file:
    #     data = file.read()
    names = all_equation_names()
    data = all_equations()
    return render_template('latex.html', names=names, data=data)

@app.route('/latex/<objname>')
def latex_by_name(objname):
    names = all_equation_names()
    data = equation_by_name(objname)
    return render_template('latex.html', names=names, data=data)