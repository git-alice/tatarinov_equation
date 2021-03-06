from scipy.integrate import RK45, odeint
from sympy import lambdify
import matplotlib.pyplot as plt
import mplcyberpunk
from tatarinov.utils.jupyter import debug_display

plt.style.use("cyberpunk")

class Integrator:
    def __init__(self, variables, equaitions):
        self.vars = variables
        self.eqs = equaitions

        self.subs_dict = None
        self.ext_subs_dict = None

        self.solution = None
        self.solution_time = None

        self.additional_eqs = None  # Уравнения, зависящие от проитегированных переменных

    def set_subs_dict(self, subs_dict, ext_subs_dict=None):
        self.subs_dict = subs_dict
        self.ext_subs_dict = ext_subs_dict if ext_subs_dict else {}

    def set_additional_eqs(self, additional_eqs):
        self.additional_eqs = additional_eqs

    def lambdify_eqs(self):
        def num_eqs(vars_values, time):
            return [lambdify(self.vars, eq.subs(self.subs_dict).doit().subs(self.ext_subs_dict), 'numpy') \
                        (*vars_values, time) for eq in self.eqs]

        return num_eqs

    def _lambdify_add_eq(self, var):
        return lambdify(self.vars,
                        self.additional_eqs[var].subs(self.subs_dict).doit().subs(self.ext_subs_dict))

    def subs_to_add_eq(self, var):
        le = self._lambdify_add_eq(var)
        return [le(*_vals, _moment) for _moment, _vals in zip(self.solution_time, self.solution[0])]

    def integrate(self, f0, time):
        solution = odeint(self.lambdify_eqs(), f0, time, full_output=True)
        self.solution = solution
        self.solution_time = time

    def plot(self, variables, f, fontsize=30):
        if type(variables) is not list:
            variables = [variables]
        for var in variables:
            if type(var) is dict:
                var_name = var.get('name')
                debug_display(f'Variable: {var_name}')
                plt.plot(self.solution_time, f(var_name))
                plt.ylabel(var.get('ylabel'), fontsize=fontsize)
                plt.xlabel(var.get('xlabel'), fontsize=fontsize)
            else:
                plt.plot(self.solution_time, f(var))
            plt.show()

    def plot_eq(self, variables):
        f = lambda var: self.solution[0][:, self.vars.index(var)]
        self.plot(variables, f)

    def plot_add_eq(self, variables):
        f = lambda var: self.subs_to_add_eq(var)
        self.plot(variables, f)
