import sympy as sp
from sympy import Symbol, solve, Eq
from sympy import diff

from tatarinov.utils.jupyter import debug_display

# TODO: Этот класс скорее всего не нужен


class MechanicalSystem:
    def __init__(self):
        self.p = None
        self.q = None
        self.constraints = None
        self.debug = True

    def set_q(self, q):
        self.q = q

    def set_p(self, p):
        self.p = p

    def poisson_bracket(self, F, G):
        """TODO надо сделать, чтобы использовалось IndexedBase"""
        """ To evaluate an unevaluated derivative, use the doit method. """
        res = 0
        for i in range(3):
            res += diff(F, self.q[i]) * diff(G, self.p[i])
            res -= diff(F, self.p[i]) * diff(G, self.q[i])
        return res

    # TODO *_Eq(s) и diff_hack нужно перенести из этого класса

    @staticmethod
    def sub_Eq(equation, eq):
        return equation.subs(eq.args[0], eq.args[1])

    @classmethod
    def sub_Eqs(cls, equation, eqs):
        sub_equation = equation
        for eq in eqs:
            sub_equation = cls.sub_Eq(sub_equation, eq)
        return sub_equation

    @staticmethod
    def left_part_Eqs(eqs):
        return [eq.args[0] for eq in eqs]

    @staticmethod
    def right_part_Eqs(eqs):
        return [eq.args[1] for eq in eqs]

    @staticmethod
    def diff_hack(equation, by):
        """ eq -> eq.subs(Derivative -> temp_variable) -> eq.diff(temp_variable) ->
            -> eq.subs(temp_variable -> Derivative)
        """
        tmp_by = Symbol('tmp_by')
        tmp_eq = equation.subs({by: tmp_by})
        tmp_eq = tmp_eq.diff(tmp_by)
        return tmp_eq.subs({tmp_by: by})

    def set_constraints(self, constraints):
        """ Setting up constraints """
        if not self.q:
            raise Exception('Значения `q` не заданы"')
        debug_display(description=f'Solving by: diff({self.q})') if self.debug else None
        solved_constraints_dict = solve(constraints, [el.diff() for el in self.q], dict=True)[0]
        solved_constraints = [Eq(k, v) for k, v in solved_constraints_dict.items()]
        self.constraints = solved_constraints

    def sub_constraints(self, func):
        """ Substitutes constraints in the equation
        Private special case:
            L -> L*
        """
        sub_dict = {conn.args[0]: conn.args[1] for conn in self.constraints}
        return func.subs(sub_dict)

    def sub_constraints_to_list(self, equations):
        return [self.sub_constraints(equation) for equation in equations]
