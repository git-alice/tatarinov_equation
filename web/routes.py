"""Route declaration."""
from flask import current_app as app
from flask import render_template

from web.control.latex import all_equations

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
    data = all_equations()
    return render_template('latex.html', data=data)


