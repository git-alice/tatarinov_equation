from tatarinov.core.mechanics import MechanicalSystem

import sympy as sp
from sympy import diff, symbols, simplify, poly, solve
from sympy import Eq, Sum, Derivative, Idx
from tatarinov.core.variables import _v, _omega, p, P, k, t

from tatarinov.utils.jupyter import display_list, display_obj, debug_display


class TatarinovSystem(MechanicalSystem):

    def __init__(self, n: int = 3, debug: bool = True):
        """

        @param n: int, Размерность системы уравнений
        @param debug: bool, Отладочный вывод
        """
        super().__init__()
        self.N = n
        self.tatarinov_equations = [None] * n
        self.debug = debug
        self.v_equations = None
        self.omega_equations = None
        self.L = None
        self.L_star = None
        self.F = None
        self.r = None
        self.Q = None
        self.P = None

    def set_omega_equations(self, omegas, equations):
        omega_equations = [Eq(omega, equation) for omega, equation in zip(omegas, equations)]
        self.omega_equations = omega_equations

    def set_v_equations(self, vs, equations):  # vs - не лучшее название
        v_equations = [Eq(v, equation) for v, equation in zip(vs, equations)]
        self.v_equations = v_equations

    def set_L(self, L):
        self.L = L

    def set_L_star(self, L_star):
        self.L_star = simplify(L_star)

    def set_F(self, F):
        self.F = F

    def create_P(self):
        equations_for_P = Eq(
            Sum(P[k] * _omega[k], (k, 1, self.N)),
            Sum(p[k] * _v[k], (k, 1, self.N)))
        if self.debug:
            debug_display(equations_for_P)
        # subs omega_i and v_i
        sub_equations_for_P = TatarinovSystem.sub_Eqs(
            equations_for_P.doit(),  # important
            self.omega_equations + self.v_equations)  # for Ex: omega[1] -> nu1), v[1] -> x', ....
        # subs_constraints
        sub_conn_equations_for_P = self.sub_constraints(sub_equations_for_P)
        if self.debug:
            debug_display(sub_conn_equations_for_P)
        # to equate the coefficients
        left_coeffs = poly(sub_conn_equations_for_P.args[0],
                           TatarinovSystem.right_part_Eqs(self.omega_equations)).coeffs()
        right_coeffs = poly(sub_conn_equations_for_P.args[1],
                            TatarinovSystem.right_part_Eqs(self.omega_equations)).coeffs()
        final_equations_for_P = [Eq(left, right) for left, right in zip(left_coeffs, right_coeffs)]
        self.P = final_equations_for_P

    def create_Q(self, r_p):
        self.Q = [self.F.dot(r_p.diff(x)) for x in self.q]

    def set_Q(self, Q):
        self.Q = Q

    def Q_dv_by_dw(self, i):
        """
        TODO: Сделать нормальное суммирование

        @param i: ???
        @return:
        """
        Q_dv_by_dw = lambda i, a: self.Q[i] * Derivative(
            self.right_part_Eqs(self.sub_constraints_to_list(self.v_equations))[i],
            self.right_part_Eqs(self.omega_equations)[a]).doit()

        def Q_dv_by_dw_sum(a):
            sum = 0
            for idx in range(len(self.q)):
                sum += Q_dv_by_dw(idx, a)
            return sum

        return Q_dv_by_dw_sum(i)

    def create_bracket_sum(self):
        """ not good """
        # return  _nu1*(p[1]*cos(alpha) + p[2]*sin(alpha)) + _nu2*(-p[1]*sin(alpha) + p[2]*cos(alpha)) + _nu3*p[3]
        bracket_sum = [_x * _y for _x, _y in
                       zip(self.right_part_Eqs(self.P), self.right_part_Eqs(self.omega_equations))]
        res = 0
        for x in range(3):
            res += bracket_sum[x]
        return res

    def tatarinov_equation(self, i):
        debug_display(description=f'Уравнение #{i}') if self.debug else None
        left = self.L_star.args[1]
        left = left.diff(self.right_part_Eqs(self.omega_equations)[i])
        left = simplify(left)
        left = left.diff(t)
        left = simplify(self.sub_constraints(left))
        _ = self.poisson_bracket(self.P[i].args[1], self.L_star.args[1])
        left += simplify(self.sub_constraints(_))
        debug_display(left, description='Левая часть уравнения') if self.debug else None

        right = self.poisson_bracket(self.P[i].args[1], self.create_bracket_sum())
        right += simplify(self.Q_dv_by_dw(i))
        debug_display(right, description='Правая часть уравнения') if self.debug else None
        ps = lambda i: self.sub_constraints(self.diff_hack(self.L.args[1], self.right_part_Eqs(self.v_equations)[i]))
        self.tatarinov_equations[i] = Eq(left, right).subs({p[1]: ps(0), p[2]: ps(1), p[3]: ps(2)})
        self.tatarinov_equations[i] = simplify(self.tatarinov_equations[i])
        return self.tatarinov_equations[i]

    def display_equations(self):
        display_list(self.tatarinov_equations)
