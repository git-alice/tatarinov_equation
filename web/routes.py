"""Route declaration."""
from flask import current_app as app
from flask import render_template

from web.control.latex import all_equations, equation_by_name, all_equation_names, all_problems

@app.route('/')
def home():
    problems = all_problems()
    return render_template('home.html',
                           title="Вэб модуль для просмотра уравнений",
                           description="Задачи: ",
                           problems=problems)

@app.route('/<problem>/latex/')
def latex(problem):
    names = all_equation_names(problem)
    data = all_equations(problem)
    return render_template('latex.html', names=names, data=data)

@app.route('/<problem>/latex/<objname>')
def latex_by_name(problem, objname):
    names = all_equation_names(problem)
    data = equation_by_name(problem, objname)
    return render_template('latex.html', names=names, data=data)